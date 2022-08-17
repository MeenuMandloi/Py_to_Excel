# import os
# my_file = '/home/my/Downloads/sample2.pdf'
# base = os.path.splitext(my_file)[0]
# os.rename(my_file, base + '.docx')

import aspose.words as aw
doc = aw.Document("/home/my/Downloads/sample2.docx")
doc.save("/home/my/Downloads/PDF.pdf")
