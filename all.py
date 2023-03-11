import tika
from tika import parser

# Initialisation de Tika
# Tika initialization
tika.initVM()


# Liste des chemins vers les fichiers à traiter
# List of paths to files to process
files_path = ['momo.pdf', 'DBSCAN.docx']

# Boucle sur les fichiers
# Loop over files
for file_path in files_path:
    # Analyse du fichier avec Tika
    # Analysis of the file with Tika
    file_content = parser.from_file(file_path)
    
    # Récupération du contenu textuel
    # Retrieval of textual content
    text_content = file_content['content']
    
    # Récupération des métadonnées
    # Metadata retrieval
    metadata = file_content['metadata']
    
    # Affichage du contenu textuel et des métadonnées
    print(f"textual content of{file_path}:")
    print(text_content)
    print("Métadonnées:")
    for cle, valeur in metadata.items():
        print(f"{cle}: {valeur}")
