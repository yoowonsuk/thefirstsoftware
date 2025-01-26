#pip install tabula-py
import tabula

table = tabula.read_pdf('weather', pages=1)
#table = tabula.read_pdf('weather', pages=2) or loop

print(type(table[0])) # <class 'pandas.core.frame.DataFrame'>

table[0].to_csv('output.csv', index=None)
