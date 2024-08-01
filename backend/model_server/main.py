import asyncio
import os
import shutil
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from pathlib import Path

import torch
import uvicorn
from fastapi import FastAPI
from transformers import logging as transformer_logging  # type:ignore

from danswer import __version__
from danswer.utils.logger import setup_logger
from model_server.custom_models import router as custom_models_router
from model_server.custom_models import warm_up_intent_model
from model_server.encoders import router as encoders_router
from model_server.encoders import warm_up_cross_encoders
from model_server.management_endpoints import router as management_router
from shared_configs.configs import ENABLE_RERANKING_ASYNC_FLOW
from shared_configs.configs import ENABLE_RERANKING_REAL_TIME_FLOW
from shared_configs.configs import INDEXING_ONLY
from shared_configs.configs import MIN_THREADS_ML_MODELS
from shared_configs.configs import MODEL_SERVER_ALLOWED_HOST
from shared_configs.configs import MODEL_SERVER_PORT

os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"

transformer_logging.set_verbosity_error()

logger = setup_logger()


async def manage_huggingface_cache() -> None:
    temp_hf_cache = Path("/root/.cache/temp_huggingface")
    hf_cache = Path("/root/.cache/huggingface")
    if temp_hf_cache.is_dir() and any(temp_hf_cache.iterdir()):
        hf_cache.mkdir(parents=True, exist_ok=True)
        for item in temp_hf_cache.iterdir():
            if item.is_dir():
                await asyncio.to_thread(
                    shutil.copytree, item, hf_cache / item.name, dirs_exist_ok=True
                )
            else:
                await asyncio.to_thread(shutil.copy2, item, hf_cache)
        await asyncio.to_thread(shutil.rmtree, temp_hf_cache)
        logger.info("Copied contents of temp_huggingface and deleted the directory.")
    else:
        logger.info("Source directory is empty or does not exist. Skipping copy.")


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    if torch.cuda.is_available():
        logger.info("GPU is available")
    else:
        logger.info("GPU is not available")

    await manage_huggingface_cache()

    torch.set_num_threads(max(MIN_THREADS_ML_MODELS, torch.get_num_threads()))
    logger.info(f"Torch Threads: {torch.get_num_threads()}")

    if not INDEXING_ONLY:
        warm_up_intent_model()
        if ENABLE_RERANKING_REAL_TIME_FLOW or ENABLE_RERANKING_ASYNC_FLOW:
            warm_up_cross_encoders()
    else:
        logger.info("This model server should only run document indexing.")

    yield


def get_model_app() -> FastAPI:
    application = FastAPI(
        title="Danswer Model Server", version=__version__, lifespan=lifespan
    )

    application.include_router(management_router)
    application.include_router(encoders_router)
    application.include_router(custom_models_router)

    return application


app = get_model_app()


if __name__ == "__main__":
    logger.info(
        f"Starting Danswer Model Server on http://{MODEL_SERVER_ALLOWED_HOST}:{str(MODEL_SERVER_PORT)}/"
    )
    logger.info(f"Model Server Version: {__version__}")
    uvicorn.run(app, host=MODEL_SERVER_ALLOWED_HOST, port=MODEL_SERVER_PORT)
