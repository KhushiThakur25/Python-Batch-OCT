import PyPDF2
from PyPDF2 import PdfReader

with open('py-pdf.pdf','rb') as file:
    pdf = PdfReader(file)
    meta_data = pdf.metadata
    pages = len(pdf.pages)
print(meta_data)
print("Number of pages present in a given pdf file:",pages)