import os

INITIAL_SEARCH_DECOMPOSITION_ENABLED = True
ALLOW_REFINEMENT = True

AGENT_DEFAULT_RETRIEVAL_HITS = 15
AGENT_DEFAULT_RERANKING_HITS = 10
AGENT_DEFAULT_SUB_QUESTION_MAX_CONTEXT_HITS = 8
AGENT_DEFAULT_NUM_DOCS_FOR_INITIAL_DECOMPOSITION = 3
AGENT_DEFAULT_NUM_DOCS_FOR_REFINED_DECOMPOSITION = 5

AGENT_DEFAULT_MAX_STREAMED_DOCS_FOR_INITIAL_ANSWER = 25
AGENT_DEFAULT_MAX_STREAMED_DOCS_FOR_REFINED_ANSWER = 35


AGENT_DEFAULT_EXPLORATORY_SEARCH_RESULTS = 5
AGENT_DEFAULT_MIN_ORIG_QUESTION_DOCS = 3
AGENT_DEFAULT_MAX_ANSWER_CONTEXT_DOCS = 10
AGENT_DEFAULT_MAX_STATIC_HISTORY_WORD_LENGTH = 2000

INITIAL_SEARCH_DECOMPOSITION_ENABLED = True
ALLOW_REFINEMENT = True

AGENT_DEFAULT_RETRIEVAL_HITS = 15
AGENT_DEFAULT_RERANKING_HITS = 10
AGENT_DEFAULT_SUB_QUESTION_MAX_CONTEXT_HITS = 8
AGENT_DEFAULT_NUM_DOCS_FOR_INITIAL_DECOMPOSITION = 3
AGENT_DEFAULT_NUM_DOCS_FOR_REFINED_DECOMPOSITION = 5
AGENT_DEFAULT_EXPLORATORY_SEARCH_RESULTS = 5
AGENT_DEFAULT_MIN_ORIG_QUESTION_DOCS = 3
AGENT_DEFAULT_MAX_ANSWER_CONTEXT_DOCS = 10
AGENT_DEFAULT_MAX_STATIC_HISTORY_WORD_LENGTH = 2000

AGENT_GENERAL_TIMEOUT = 600   # 10 mn in seconds

AGENT_ANSWER_GENERATION_BY_FAST_LLM = (
    os.environ.get("AGENT_ANSWER_GENERATION_BY_FAST_LLM", "").lower() == "true"
)

AGENT_RETRIEVAL_STATS = (
    not os.environ.get("AGENT_RETRIEVAL_STATS") == "False"
) or True  # default True


AGENT_MAX_QUERY_RETRIEVAL_RESULTS = int(
    os.environ.get("AGENT_MAX_QUERY_RETRIEVAL_RESULTS") or AGENT_DEFAULT_RETRIEVAL_HITS
)  # 15

AGENT_MAX_QUERY_RETRIEVAL_RESULTS = int(
    os.environ.get("AGENT_MAX_QUERY_RETRIEVAL_RESULTS") or AGENT_DEFAULT_RETRIEVAL_HITS
)  # 15

# Reranking agent configs
# Reranking stats - no influence on flow outside of stats collection
AGENT_RERANKING_STATS = (
    not os.environ.get("AGENT_RERANKING_STATS") == "True"
) or False  # default False

AGENT_MAX_QUERY_RETRIEVAL_RESULTS = int(
    os.environ.get("AGENT_MAX_QUERY_RETRIEVAL_RESULTS") or AGENT_DEFAULT_RETRIEVAL_HITS
)  # 15

AGENT_RERANKING_MAX_QUERY_RETRIEVAL_RESULTS = int(
    os.environ.get("AGENT_RERANKING_MAX_QUERY_RETRIEVAL_RESULTS")
    or AGENT_DEFAULT_RERANKING_HITS
)  # 10

AGENT_NUM_DOCS_FOR_DECOMPOSITION = int(
    os.environ.get("AGENT_NUM_DOCS_FOR_DECOMPOSITION")
    or AGENT_DEFAULT_NUM_DOCS_FOR_INITIAL_DECOMPOSITION
)  # 3

AGENT_NUM_DOCS_FOR_REFINED_DECOMPOSITION = int(
    os.environ.get("AGENT_NUM_DOCS_FOR_REFINED_DECOMPOSITION")
    or AGENT_DEFAULT_NUM_DOCS_FOR_REFINED_DECOMPOSITION
)  # 5

AGENT_EXPLORATORY_SEARCH_RESULTS = int(
    os.environ.get("AGENT_EXPLORATORY_SEARCH_RESULTS")
    or AGENT_DEFAULT_EXPLORATORY_SEARCH_RESULTS
)  # 5

AGENT_MIN_ORIG_QUESTION_DOCS = int(
    os.environ.get("AGENT_MIN_ORIG_QUESTION_DOCS")
    or AGENT_DEFAULT_MIN_ORIG_QUESTION_DOCS
)  # 3

AGENT_MAX_ANSWER_CONTEXT_DOCS = int(
    os.environ.get("AGENT_MAX_ANSWER_CONTEXT_DOCS")
    or AGENT_DEFAULT_SUB_QUESTION_MAX_CONTEXT_HITS
)  # 8


AGENT_MAX_STATIC_HISTORY_WORD_LENGTH = int(
    os.environ.get("AGENT_MAX_STATIC_HISTORY_WORD_LENGTH")
    or AGENT_DEFAULT_MAX_STATIC_HISTORY_WORD_LENGTH
)  # 2000

AGENT_MAX_STREAMED_DOCS_FOR_INITIAL_ANSWER = int(
    os.environ.get("AGENT_MAX_STREAMED_DOCS_FOR_INITIAL_ANSWER")
    or AGENT_DEFAULT_MAX_STREAMED_DOCS_FOR_INITIAL_ANSWER
)  # 25

AGENT_MAX_STREAMED_DOCS_FOR_REFINED_ANSWER = int(
    os.environ.get("AGENT_MAX_STREAMED_DOCS_FOR_REFINED_ANSWER")
    or AGENT_DEFAULT_MAX_STREAMED_DOCS_FOR_REFINED_ANSWER
)  # 35


AGENT_RETRIEVAL_STATS = (
    not os.environ.get("AGENT_RETRIEVAL_STATS") == "False"
) or True  # default True


AGENT_MAX_QUERY_RETRIEVAL_RESULTS = int(
    os.environ.get("AGENT_MAX_QUERY_RETRIEVAL_RESULTS") or AGENT_DEFAULT_RETRIEVAL_HITS
)  # 15

AGENT_MAX_QUERY_RETRIEVAL_RESULTS = int(
    os.environ.get("AGENT_MAX_QUERY_RETRIEVAL_RESULTS") or AGENT_DEFAULT_RETRIEVAL_HITS
)  # 15

# Reranking agent configs
# Reranking stats - no influence on flow outside of stats collection
AGENT_RERANKING_STATS = (
    not os.environ.get("AGENT_RERANKING_STATS") == "True"
) or False  # default False

AGENT_MAX_QUERY_RETRIEVAL_RESULTS = int(
    os.environ.get("AGENT_MAX_QUERY_RETRIEVAL_RESULTS") or AGENT_DEFAULT_RETRIEVAL_HITS
)  # 15

AGENT_RERANKING_MAX_QUERY_RETRIEVAL_RESULTS = int(
    os.environ.get("AGENT_RERANKING_MAX_QUERY_RETRIEVAL_RESULTS")
    or AGENT_DEFAULT_RERANKING_HITS
)  # 10

AGENT_NUM_DOCS_FOR_DECOMPOSITION = int(
    os.environ.get("AGENT_NUM_DOCS_FOR_DECOMPOSITION")
    or AGENT_DEFAULT_NUM_DOCS_FOR_INITIAL_DECOMPOSITION
)  # 3

AGENT_NUM_DOCS_FOR_REFINED_DECOMPOSITION = int(
    os.environ.get("AGENT_NUM_DOCS_FOR_REFINED_DECOMPOSITION")
    or AGENT_DEFAULT_NUM_DOCS_FOR_REFINED_DECOMPOSITION
)  # 5

AGENT_EXPLORATORY_SEARCH_RESULTS = int(
    os.environ.get("AGENT_EXPLORATORY_SEARCH_RESULTS")
    or AGENT_DEFAULT_EXPLORATORY_SEARCH_RESULTS
)  # 5

AGENT_MIN_ORIG_QUESTION_DOCS = int(
    os.environ.get("AGENT_MIN_ORIG_QUESTION_DOCS")
    or AGENT_DEFAULT_MIN_ORIG_QUESTION_DOCS
)  # 3

AGENT_MAX_ANSWER_CONTEXT_DOCS = int(
    os.environ.get("AGENT_MAX_ANSWER_CONTEXT_DOCS")
    or AGENT_DEFAULT_SUB_QUESTION_MAX_CONTEXT_HITS
)  # 8


AGENT_MAX_STATIC_HISTORY_WORD_LENGTH = int(
    os.environ.get("AGENT_MAX_STATIC_HISTORY_WORD_LENGTH")
    or AGENT_DEFAULT_MAX_STATIC_HISTORY_WORD_LENGTH
)  # 2000


AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_ENTITY_TERM_EXTRACTION = AGENT_GENERAL_TIMEOUT  # in seconds
AGENT_TIMEOUT_CONNECT_LLM_ENTITY_TERM_EXTRACTION = int(
    os.environ.get("AGENT_TIMEOUT_CONNECT_LLM_ENTITY_TERM_EXTRACTION")
    or AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_ENTITY_TERM_EXTRACTION
)

AGENT_DEFAULT_TIMEOUT_LLM_ENTITY_TERM_EXTRACTION = AGENT_GENERAL_TIMEOUT  # in seconds
AGENT_TIMEOUT_LLM_ENTITY_TERM_EXTRACTION = int(
    os.environ.get("AGENT_TIMEOUT_LLM_ENTITY_TERM_EXTRACTION")
    or AGENT_DEFAULT_TIMEOUT_LLM_ENTITY_TERM_EXTRACTION
)


AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_DOCUMENT_VERIFICATION = AGENT_GENERAL_TIMEOUT  # in seconds
AGENT_TIMEOUT_CONNECT_LLM_DOCUMENT_VERIFICATION = int(
    os.environ.get("AGENT_TIMEOUT_CONNECT_LLM_DOCUMENT_VERIFICATION")
    or AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_DOCUMENT_VERIFICATION
)

AGENT_DEFAULT_TIMEOUT_LLM_DOCUMENT_VERIFICATION = AGENT_GENERAL_TIMEOUT #AGENT_GENERAL_TIMEOUT  # in seconds
AGENT_TIMEOUT_LLM_DOCUMENT_VERIFICATION = int(
    os.environ.get("AGENT_TIMEOUT_LLM_DOCUMENT_VERIFICATION")
    or AGENT_DEFAULT_TIMEOUT_LLM_DOCUMENT_VERIFICATION
)


AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_GENERAL_GENERATION = AGENT_GENERAL_TIMEOUT  # in seconds
AGENT_TIMEOUT_CONNECT_LLM_GENERAL_GENERATION = int(
    os.environ.get("AGENT_TIMEOUT_CONNECT_LLM_GENERAL_GENERATION")
    or AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_GENERAL_GENERATION
)

AGENT_DEFAULT_TIMEOUT_LLM_GENERAL_GENERATION = AGENT_GENERAL_TIMEOUT  # in seconds
AGENT_TIMEOUT_LLM_GENERAL_GENERATION = int(
    os.environ.get("AGENT_TIMEOUT_LLM_GENERAL_GENERATION")
    or AGENT_DEFAULT_TIMEOUT_LLM_GENERAL_GENERATION
)


AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_SUBQUESTION_GENERATION = AGENT_GENERAL_TIMEOUT # in seconds
AGENT_TIMEOUT_CONNECT_LLM_SUBQUESTION_GENERATION = int(
    os.environ.get("AGENT_TIMEOUT_CONNECT_LLM_SUBQUESTION_GENERATION")
    or AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_SUBQUESTION_GENERATION
)

AGENT_DEFAULT_TIMEOUT_LLM_SUBQUESTION_GENERATION = AGENT_GENERAL_TIMEOUT  # in seconds
AGENT_TIMEOUT_LLM_SUBQUESTION_GENERATION = int(
    os.environ.get("AGENT_TIMEOUT_LLM_SUBQUESTION_GENERATION")
    or AGENT_DEFAULT_TIMEOUT_LLM_SUBQUESTION_GENERATION
)


AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_SUBANSWER_GENERATION = AGENT_GENERAL_TIMEOUT  # in seconds
AGENT_TIMEOUT_CONNECT_LLM_SUBANSWER_GENERATION = int(
    os.environ.get("AGENT_TIMEOUT_CONNECT_LLM_SUBANSWER_GENERATION")
    or AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_SUBANSWER_GENERATION
)

AGENT_DEFAULT_TIMEOUT_LLM_SUBANSWER_GENERATION = AGENT_GENERAL_TIMEOUT  # in seconds
AGENT_TIMEOUT_LLM_SUBANSWER_GENERATION = int(
    os.environ.get("AGENT_TIMEOUT_LLM_SUBANSWER_GENERATION")
    or AGENT_DEFAULT_TIMEOUT_LLM_SUBANSWER_GENERATION
)


AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_INITIAL_ANSWER_GENERATION = AGENT_GENERAL_TIMEOUT  # in seconds
AGENT_TIMEOUT_CONNECT_LLM_INITIAL_ANSWER_GENERATION = int(
    os.environ.get("AGENT_TIMEOUT_CONNECT_LLM_INITIAL_ANSWER_GENERATION")
    or AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_INITIAL_ANSWER_GENERATION
)

AGENT_DEFAULT_TIMEOUT_LLM_INITIAL_ANSWER_GENERATION = AGENT_GENERAL_TIMEOUT  # in seconds
AGENT_TIMEOUT_LLM_INITIAL_ANSWER_GENERATION = int(
    os.environ.get("AGENT_TIMEOUT_LLM_INITIAL_ANSWER_GENERATION")
    or AGENT_DEFAULT_TIMEOUT_LLM_INITIAL_ANSWER_GENERATION
)


AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_REFINED_ANSWER_GENERATION = AGENT_GENERAL_TIMEOUT  # in seconds
AGENT_TIMEOUT_CONNECT_LLM_REFINED_ANSWER_GENERATION = int(
    os.environ.get("AGENT_TIMEOUT_CONNECT_LLM_REFINED_ANSWER_GENERATION")
    or AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_REFINED_ANSWER_GENERATION
)

AGENT_DEFAULT_TIMEOUT_LLM_REFINED_ANSWER_GENERATION = AGENT_GENERAL_TIMEOUT  # in seconds
AGENT_TIMEOUT_LLM_REFINED_ANSWER_GENERATION = int(
    os.environ.get("AGENT_TIMEOUT_LLM_REFINED_ANSWER_GENERATION")
    or AGENT_DEFAULT_TIMEOUT_LLM_REFINED_ANSWER_GENERATION
)


AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_SUBANSWER_CHECK = AGENT_GENERAL_TIMEOUT  # in seconds
AGENT_TIMEOUT_CONNECT_LLM_SUBANSWER_CHECK = int(
    os.environ.get("AGENT_TIMEOUT_CONNECT_LLM_SUBANSWER_CHECK")
    or AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_SUBANSWER_CHECK
)

AGENT_DEFAULT_TIMEOUT_LLM_SUBANSWER_CHECK = AGENT_GENERAL_TIMEOUT  # in seconds
AGENT_TIMEOUT_LLM_SUBANSWER_CHECK = int(
    os.environ.get("AGENT_TIMEOUT_LLM_SUBANSWER_CHECK")
    or AGENT_DEFAULT_TIMEOUT_LLM_SUBANSWER_CHECK
)


AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_REFINED_SUBQUESTION_GENERATION = AGENT_GENERAL_TIMEOUT  # in seconds
AGENT_TIMEOUT_CONNECT_LLM_REFINED_SUBQUESTION_GENERATION = int(
    os.environ.get("AGENT_TIMEOUT_CONNECT_LLM_REFINED_SUBQUESTION_GENERATION")
    or AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_REFINED_SUBQUESTION_GENERATION
)

AGENT_DEFAULT_TIMEOUT_LLM_REFINED_SUBQUESTION_GENERATION = AGENT_GENERAL_TIMEOUT  # in seconds
AGENT_TIMEOUT_LLM_REFINED_SUBQUESTION_GENERATION = int(
    os.environ.get("AGENT_TIMEOUT_LLM_REFINED_SUBQUESTION_GENERATION")
    or AGENT_DEFAULT_TIMEOUT_LLM_REFINED_SUBQUESTION_GENERATION
)


AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_QUERY_REWRITING_GENERATION = AGENT_GENERAL_TIMEOUT  # in seconds
AGENT_TIMEOUT_CONNECT_LLM_QUERY_REWRITING_GENERATION = int(
    os.environ.get("AGENT_TIMEOUT_CONNECT_LLM_QUERY_REWRITING_GENERATION")
    or AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_QUERY_REWRITING_GENERATION
)

AGENT_DEFAULT_TIMEOUT_LLM_QUERY_REWRITING_GENERATION = AGENT_GENERAL_TIMEOUT  # in seconds
AGENT_TIMEOUT_LLM_QUERY_REWRITING_GENERATION = int(
    os.environ.get("AGENT_TIMEOUT_LLM_QUERY_REWRITING_GENERATION")
    or AGENT_DEFAULT_TIMEOUT_LLM_QUERY_REWRITING_GENERATION
)


AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_HISTORY_SUMMARY_GENERATION = AGENT_GENERAL_TIMEOUT  # in seconds
AGENT_TIMEOUT_CONNECT_LLM_HISTORY_SUMMARY_GENERATION = int(
    os.environ.get("AGENT_TIMEOUT_CONNECT_LLM_HISTORY_SUMMARY_GENERATION")
    or AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_HISTORY_SUMMARY_GENERATION
)

AGENT_DEFAULT_TIMEOUT_LLM_HISTORY_SUMMARY_GENERATION = AGENT_GENERAL_TIMEOUT  # in seconds
AGENT_TIMEOUT_LLM_HISTORY_SUMMARY_GENERATION = int(
    os.environ.get("AGENT_TIMEOUT_LLM_HISTORY_SUMMARY_GENERATION")
    or AGENT_DEFAULT_TIMEOUT_LLM_HISTORY_SUMMARY_GENERATION
)


AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_COMPARE_ANSWERS = AGENT_GENERAL_TIMEOUT  # in seconds
AGENT_TIMEOUT_CONNECT_LLM_COMPARE_ANSWERS = int(
    os.environ.get("AGENT_TIMEOUT_CONNECT_LLM_COMPARE_ANSWERS")
    or AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_COMPARE_ANSWERS
)

AGENT_DEFAULT_TIMEOUT_LLM_COMPARE_ANSWERS = AGENT_GENERAL_TIMEOUT  # in seconds
AGENT_TIMEOUT_LLM_COMPARE_ANSWERS = int(
    os.environ.get("AGENT_TIMEOUT_LLM_COMPARE_ANSWERS")
    or AGENT_DEFAULT_TIMEOUT_LLM_COMPARE_ANSWERS
)


AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_REFINED_ANSWER_VALIDATION = AGENT_GENERAL_TIMEOUT  # in seconds
AGENT_TIMEOUT_CONNECT_LLM_REFINED_ANSWER_VALIDATION = int(
    os.environ.get("AGENT_TIMEOUT_CONNECT_LLM_REFINED_ANSWER_VALIDATION")
    or AGENT_DEFAULT_TIMEOUT_CONNECT_LLM_REFINED_ANSWER_VALIDATION
)

AGENT_DEFAULT_TIMEOUT_LLM_REFINED_ANSWER_VALIDATION = AGENT_GENERAL_TIMEOUT  # in seconds
AGENT_TIMEOUT_LLM_REFINED_ANSWER_VALIDATION = int(
    os.environ.get("AGENT_TIMEOUT_LLM_REFINED_ANSWER_VALIDATION")
    or AGENT_DEFAULT_TIMEOUT_LLM_REFINED_ANSWER_VALIDATION
)

AGENT_DEFAULT_MAX_TOKENS_VALIDATION = 4
AGENT_MAX_TOKENS_VALIDATION = int(
    os.environ.get("AGENT_MAX_TOKENS_VALIDATION") or AGENT_DEFAULT_MAX_TOKENS_VALIDATION
)

AGENT_DEFAULT_MAX_TOKENS_SUBANSWER_GENERATION = 256
AGENT_MAX_TOKENS_SUBANSWER_GENERATION = int(
    os.environ.get("AGENT_MAX_TOKENS_SUBANSWER_GENERATION")
    or AGENT_DEFAULT_MAX_TOKENS_SUBANSWER_GENERATION
)

AGENT_DEFAULT_MAX_TOKENS_ANSWER_GENERATION = 1024
AGENT_MAX_TOKENS_ANSWER_GENERATION = int(
    os.environ.get("AGENT_MAX_TOKENS_ANSWER_GENERATION")
    or AGENT_DEFAULT_MAX_TOKENS_ANSWER_GENERATION
)

AGENT_DEFAULT_MAX_TOKENS_SUBQUESTION_GENERATION = 256
AGENT_MAX_TOKENS_SUBQUESTION_GENERATION = int(
    os.environ.get("AGENT_MAX_TOKENS_SUBQUESTION_GENERATION")
    or AGENT_DEFAULT_MAX_TOKENS_SUBQUESTION_GENERATION
)

AGENT_DEFAULT_MAX_TOKENS_ENTITY_TERM_EXTRACTION = 1024
AGENT_MAX_TOKENS_ENTITY_TERM_EXTRACTION = int(
    os.environ.get("AGENT_MAX_TOKENS_ENTITY_TERM_EXTRACTION")
    or AGENT_DEFAULT_MAX_TOKENS_ENTITY_TERM_EXTRACTION
)

AGENT_DEFAULT_MAX_TOKENS_SUBQUERY_GENERATION = 64
AGENT_MAX_TOKENS_SUBQUERY_GENERATION = int(
    os.environ.get("AGENT_MAX_TOKENS_SUBQUERY_GENERATION")
    or AGENT_DEFAULT_MAX_TOKENS_SUBQUERY_GENERATION
)

AGENT_DEFAULT_MAX_TOKENS_HISTORY_SUMMARY = 128
AGENT_MAX_TOKENS_HISTORY_SUMMARY = int(
    os.environ.get("AGENT_MAX_TOKENS_HISTORY_SUMMARY")
    or AGENT_DEFAULT_MAX_TOKENS_HISTORY_SUMMARY
)

GRAPH_VERSION_NAME: str = "a"
