from fpdf import FPDF

pdf = FPDF(orientation="P", unit='pt', format='A4')
pdf.add_page()


#packages -> fpdf => from fpdf imprt FPDF => help(fpdf) or dir(fpdf)
pdf.image('tiger.jpeg', w=80, h=50, x=500)

pdf.set_font(family='Times', style='B', size=24)
pdf.cell(w=0, h=50, txt='Malayan Tiger', aglin='C', border=1, ln=1)
#pdf.cell(w=200, h=50, txt='Malayan Tiger', aglin='C', border=1)

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=0, h=15, txt='Description', ln=1, border=1)


# https://en.wikipedia.org/wiki/Malayan_tiger
pdf.set_font(family='Times', size=14)
txt1="""
The Malayan tiger is a tiger from a specific population of the Panthera tigris tigris subspecies that is native to Peninsular Malaysia.[2] This population inhabits the southern and central parts of the Malay Peninsula, and has been classified as critically endangered. As of April 2014, the population was estimated at 80–120 mature individuals, with a continuing downward trend
"""
pdf.multi_cell(w=0, h=15, txt=txt1)

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=100, h=25, txt='Kingdom: ')

pdf.set_font(family='Times', size=14)
pdf.cell(w=100, h=25, txt='Animalia', ln=1)


pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=100, h=25, txt='Phylum: ')

pdf.set_font(family='Times', size=14)
pdf.cell(w=100, h=25, txt='Chordata', ln=1)



pdf.output('output.pdf')
