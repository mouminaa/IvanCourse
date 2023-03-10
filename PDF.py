import PyPDF2

# Ouverture du fichier PDF
with open('momo.pdf', 'rb') as fichier:
    # Instanciation de l'objet PdfFileReader
    pdf_reader = PyPDF2.PdfFileReader(fichier)
    
    # Boucle sur toutes les pages du PDF
    for num_page in range(pdf_reader.getNumPages()):
        # Récupération du contenu textuel de la page
        page = pdf_reader.getPage(num_page)
        contenu = page.extractText()
        
        # Affichage du contenu textuel de la page
        print(contenu)
