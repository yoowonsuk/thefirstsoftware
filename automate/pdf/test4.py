import tabula #pip install openpyxl
 
table = tabula.read_pdf('Table and Text.pdf', pages=1)
table[0].to_excel('output.xlsx', index=None)
