from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileWriter, PdfFileReader
import os
"""
Refer to an image if you want to add an image to a watermark.
Fill in text if you want to watermark with text.
Alternatively, following settings will skip this.
picture_path = None
text = None
"""

text = 'Cubexo'
# Folder in which PDF files will be watermarked. (Could be shared folder)
folder_path = './home/my/Downloads/'
c = canvas.Canvas('watermark.pdf')
if text:
    c.setFontSize(50)
    c.setFont('Helvetica-Bold', 36)
    c.drawString(30, 30, text)

    c.save()
watermark = PdfFileReader(open("watermark.pdf", "rb"))
for file in os.listdir("/home/my/Downloads/"):
    if file.endswith(".pdf"):
        output_file = PdfFileWriter()
        input_file = PdfFileReader(open("/home/my/Downloads" + "/" + "theory-lectures-v2.pdf", "rb"))
        page_count = input_file.getNumPages()
for page_number in range(30):
    input_page = input_file.getPage(page_number)
    input_page.mergePage(watermark.getPage(0))
    output_file.addPage(input_page)
    output_path = "/home/my/Downloads" + '/' + file.split('.pdf')[0] + '_watermarked' + '.pdf'
    with open(output_path, "wb") as outputStream:
        output_file.write(outputStream)
