from io import BytesIO
from docx import Document
from fpdf import FPDF

def create_pdf(text):

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in text.split('\n'):
        pdf.multi_cell(0, 10, line)
    pdf_output = BytesIO()
    pdf.output(pdf_output, 'F')
    pdf_output.seek(0)

    return pdf_output.read()

def create_word(text):

    doc = Document()
    doc.add_paragraph(text)
    word_output = BytesIO()
    doc.save(word_output)
    word_output.seek(0)
    
    return word_output.read()