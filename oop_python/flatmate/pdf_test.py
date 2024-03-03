from fpdf import FPDF

# scratches and consoles

pdf = FPDF(orientation='P', unit='pt', format = 'A4') # pt = point, 12points = 16pixels
pdf.add_page()

# Add some text
pdf.set_font(family='Times', size=24, style='B')
pdf.cell(w=100, h=80, txt='Flatmates Bill', border=1, align="C")) # unit = pt, center
pdf.cell(w=50, h=40, txt="Period", border = 1)

pdf.output("bill.pdf")
#camtasia

