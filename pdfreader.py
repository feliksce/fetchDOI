from PyPDF2 import PdfFileReader as readpdf
import os
import re
# import requests

dir = "pub_phi_article/"
list_of_pdfs = [file for file in os.listdir(dir) if file.endswith(".pdf")]

for each in list_of_pdfs:
    path = dir + each
    pdf = open(path, "rb")
    pdf_data = readpdf(pdf, strict=False).getDocumentInfo()
    # pdf_xmp = readpdf(pdf, strict=False).getXmpMetadata()
    out = re.search("doi:[\w.,/]+", str(pdf_data))
    try:
        print(path, out.group()[4:])
    except AttributeError:
        print(None)
    # try:
    #     # doi_number = pdf_xmp.custom_properties["doi"]
    #     # print(path, doi_number)
    # except KeyError:
    #     print("{}: cannot find DOI number!".format(path))
    #     continue


# # find DOI number form pdf
# fname = "Gardner2017.pdf"
# pdf = open(fname, "rb")
#
# pdf_data = readpdf(pdf, strict=False).getDocumentInfo()
# pdf_xmp = readpdf(pdf, strict=False).getXmpMetadata()
# doi_number = pdf_xmp.custom_properties["doi"]

# # read webpage
# address = "http://dx.doi.org/{}".format(doi_number)
# print("Fetching data from address: {}".format(address))
# request = requests.get(address)
# print(request.url)
# address = request.url
# request = requests.get(address)
# print(request.url)
