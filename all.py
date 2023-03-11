import tika
from tika import parser

# Initialisation de Tika
tika.initVM()

# Liste des chemins vers les fichiers à traiter
chemins_fichiers = ['momo.pdf', 'DBSCAN.docx']

# Boucle sur les fichiers
for chemin_fichier in chemins_fichiers:
    # Analyse du fichier avec Tika
    contenu_fichier = parser.from_file(chemin_fichier)
    
    # Récupération du contenu textuel
    contenu_textuel = contenu_fichier['content']
    
    # Récupération des métadonnées
    metadonnees = contenu_fichier['metadata']
    
    # Affichage du contenu textuel et des métadonnées
    print(f"Contenu textuel de {chemin_fichier}:")
    print(contenu_textuel)
    print("Métadonnées:")
    for cle, valeur in metadonnees.items():
        print(f"{cle}: {valeur}")
