from PyPDF2 import PdfFileReader as readpdf
import re

# fname = "weil2006.pdf"
fname = "petasis2015.pdf"
pdf = open(fname, "rb")

pdf_data = readpdf(pdf, strict=False).getDocumentInfo()

# print_labels = {"Author: ": pdf_data.author,
#                 # "Author raw ": pdf_data.author_raw,
#                 "Creator: ": pdf_data.creator,
#                 # "Creator raw: ": pdf_data.creator_raw,
#                 "Producer: ": pdf_data.producer,
#                 # "Producer raw: ": pdf_data.producer_raw,
#                 "Subject: ": pdf_data.subject,
#                 # "Subject raw: ": pdf_data.subject_raw,
#                 "Title: ": pdf_data.title,
#                 # "Title raw: ": pdf_data.title_raw
#                 }
# jak wyciągnąć rok z pola subject
# print(pdf_data.subject)
# year = re.findall(r"\((\d{4})\)", str(pdf_data.subject))[0]
# print(year)

# for key, value in print_labels.items():
#     print(key, str(value))
#
# pdf_xmp = readpdf(pdf, strict=False).getXmpMetadata()
# print(pdf_xmp.custom_properties)  # zwraca dict

#
# tak wyciągniesz DOI
pdf_xmp = readpdf(pdf, strict=False).getXmpMetadata()
print(pdf_xmp.custom_properties["doi"])
