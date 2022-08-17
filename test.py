from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

pdf_file = "/home/my/Downloads/theory-lectures-v2.pdf"
watermark = "/home/my/Downloads/watermark.pdf"
merged = "/home/my/Downloads/merged_file.pdf"

with open(watermark, "rb") as watermark_file, open(pdf_file, "rb") as input_file:
    watermark_pdf = PdfFileReader(watermark_file)
    input_pdf = PdfFileReader(input_file)
    watermark_page = watermark_pdf.getPage(0)

    output = PdfFileWriter()

    for i in range(input_pdf.getNumPages()):
        pdf_page = input_pdf.getPage(i)
        watermark_page.mergePage(pdf_page)
        output.addPage(watermark_page

    with open(merged, "wb") as merged_file:
        output.write(merged_file)
