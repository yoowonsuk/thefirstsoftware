import webbrowser

from fpdf import FPDF
from filestack import Client


class Bill:
    """
    Object that contains data about a bill, such as total
    amount and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate person who lives in the flat
    and pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.days_in_house = days_in_house
        self.name = name

    def pays(self, bill, flatmate2):
        return bill.amount * \
            (self.days_in_house/(self.days_in_house+flatmate2.days_in_house))


class PdfReport:
    """
    Creates a Pdf file that contains data about
    the flatmates such as their names, their due amout
    and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        pdf = FPDF(orientation='P', unit='pt', format='A4')  # pt = point, 12points = 16pixels
        pdf.add_page()

        # Add icon
        pdf.image("house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align="C", ln=1)  # unit = pt, center

        # Insert Period label and value
        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period:", border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=str(round(flatmate1.pays(bill=bill, flatmate2=flatmate2),2 )), border=0, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=str(round(flatmate2.pays(bill=bill, flatmate2=flatmate1),2 )), border=0, ln=1)

        pdf.output(self.filename)
        webbrowser.open(self.filename)
        # Linux or Mac
        # webbrowser.open('file://' + os.path.realpath(self.filename))

class FileSharer: #open for extension and closed for modification

    def __init__(self, filepath, api_key="something"): # alt + enter
        self.api_key = api_key
        self.filepath = filepath

    def share(self):
        client = Client(self.api_key)

        new_filelink = client.upload(filepath=filepath=self.filepath)
        #print(type(new_filelink))
        #print(new_filelink.url)
        return new_filelink.url

