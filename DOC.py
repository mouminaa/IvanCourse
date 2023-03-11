import docx

# Ouverture du fichier DOCX
document = docx.Document('Ivancours.docx')

# Boucle sur tous les paragraphes du document

for paragraphe in document.paragraphs:
    # Récupération du contenu textuel du paragraphe
    contenu = paragraphe.text
    
    # Affichage du contenu textuel du paragraphe
    print(contenu)
