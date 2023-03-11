import PyPDF2

pdf_file = open("momo.pdf", "rb")
pdf_reader = PyPDF2.PdfReader(pdf_file)
page = pdf_reader.pages[0]

text = page.extract_text()
print(text)

width = page.mediabox[2]
height = page.mediabox[3]
print(f"Page width: {width}")
print(f"Page height: {height}")

