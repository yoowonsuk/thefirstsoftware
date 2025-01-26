# Package PyMuPDF

import fitz

with fitz.open("students.pdf") as pdf:
    text = ''
    for page in pdf:
        print(20*'-')
        print(page.get_text())
        #text = text + page.get_text()

with fitz.open("students.pdf") as pdf:
    page1 = pdf[0].get_text()
    print(page1)
