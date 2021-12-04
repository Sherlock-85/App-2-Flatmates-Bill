import webbrowser
import os

from fpdf import FPDF


class PdfReport:
    """
    Creates a Pdf file that contains the names
    and amounts due for each flatmate. Also contains the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatemate1, flatmate2, bill):
        flatmate1_pays = str(round(flatemate1.pays(bill=bill, flatmate2=flatmate2), 2))
        flatmate2_pays = str(round(flatmate2.pays(bill=bill, flatmate2=flatemate1), 2))
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add house icon
        pdf.image('files/house.png', w=40, h=40)

        # Add title
        pdf.set_font(family="Arial", style="B", size=24)
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)
        # Add period label and value
        pdf.set_font(family="Arial", style="B", size=16)
        pdf.cell(w=100, h=40, txt="Period:", border=0, align="L")
        pdf.cell(w=175, h=40, txt=bill.period, border=0, align="L", ln=1)
        # Add the first flatmate's name and amount paid
        pdf.set_font(family="Arial", style="", size=16)
        pdf.cell(w=100, h=40, txt=flatemate1.name, border=0, align="L")
        pdf.cell(w=175, h=40, txt="Amount Paid: $" +flatmate1_pays, border=0, align="L", ln=1)
        # Add the second flatmate's name and amount paid
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=0, align="L")
        pdf.cell(w=175, h=40, txt="Amount Paid: $" +flatmate2_pays, border=0, align="L", ln=1)

        # Change Directory to files, generate and open PDF.
        os.chdir("files")
        pdf.output(self.filename)
        webbrowser.open(self.filename)