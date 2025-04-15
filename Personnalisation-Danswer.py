import os
import re

# Chemins des fichiers à modifier
files_to_modify = [
    "web/src/components/logo/FixedLogo.tsx",
    "web/src/components/header/LogoType.tsx",
    "web/src/app/chat/shared_chat_search/FixedLogo.tsx",
    "web/src/components/admin/connectors/AdminSidebar.tsx",
]

# Le texte à rechercher
search_text = r'Powered by Onyx'
#search_text = r"L&apos;IAssistant Médical"

# Le texte de remplacement
#replace_text = "IAssistant"
replace_text = "L&apos;IAssistant Médical"

def replace_text_in_file(file_path, search_text, replace_text):
    # Lire le contenu du fichier
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Vérifier s'il y a des correspondances
    if re.search(search_text, content):
        # Remplacer le texte
        updated_content = re.sub(search_text, replace_text, content)

        # Écrire le contenu modifié dans le fichier
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)
        print(f"Texte remplacé dans {file_path}")
    else:
        print(f"Aucune correspondance trouvée dans {file_path}")

# Parcourir les fichiers et appliquer la fonction
for file_path in files_to_modify:
    if os.path.exists(file_path):
        replace_text_in_file(file_path, search_text, replace_text)
    else:
        print(f"Le fichier {file_path} n'existe pas.")
