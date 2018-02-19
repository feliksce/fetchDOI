# fetchDOI v.0.1
# actually done

# TODO input file
# TODO iteration over input dir
# TODO Err handlers
# TODO defs for other functions
# TODO renaming input files
# TODO two naming modes: PC "AuthorYear" and CR "Author_journal_vol_1stpage_yr"

import requests
import json
import re
import os
import sys
from PyPDF2 import PdfFileReader as readpdf


# def get_doi_number_from_pdf(pdf_file):
#     pdf = open(pdf_file, "rb")
#     pdf_xmp = readpdf(pdf, strict=False).getXmpMetadata()
#     doi_number = pdf_xmp.custom_properties["doi"]
#     pdf.close()
#     return doi_number


def get_doi_number_from_pdf(pdf_file):
    print("File: {}".format(pdf_file))
    pdf = open(pdf_file, "rb")
    pdf_data = readpdf(pdf, strict=False).getDocumentInfo()
    out = re.search("(?i)(doi:)[\w.,/]+", str(pdf_data))
    # TODO if not in properties, maybe find in text? add text search
    try:
        doi_number = out.group()[4:]
        print("DOI:{}".format(doi_number))
        return doi_number
    except AttributeError:
        print("DOI: Cannot find DOI number!")
        return False


def fetch_doi_message(doi_number):
    if doi_number:
        address = "https://api.crossref.org/works/{}".format(doi_number)
        print("Fetching data from address: {}".format(address))
        request = requests.get(address)
        output = request.text
        pretty_output = json.loads(output)
        message = pretty_output['message']
        if message:
            return message


# author_journal_vol_1stpage_yr
def construct_name(message):
    # TODO put try blocks on each line
    if message:
        author_surname = message['author'][0]['family'].split(" ")[-1]
        # TODO automatic search for joucode
        journal = message['short-container-title'][0]
        volume = message['volume']
        first_page = message['page'].split("-")[0]
        year = message['indexed']['date-parts'][0][0]
        # year = False

        return str("{}_{}_{}_{}_{}".format(author_surname, journal, volume, first_page, year))


def show_doi_webpage(doi_number):
    # TODO open webpage in browser
    pass


def print_names(list_of_pdfs):
    for file in list_of_pdfs:
        doi_number = get_doi_number_from_pdf(file)
        if not doi_number: pass
        message = fetch_doi_message(doi_number)
        fn = construct_name(message)
        print("File name:\t\t{}".format(fn))
        print("____________________\n")

if __name__ == "__main__":

    try:
        # TODO finishes too early, do something with path
        files = input("Input filepath or directory:\n")
        if os.path.isdir(files):
            list_of_pdfs = [files + file for file in os.listdir(files) if file.endswith(".pdf")]
            print_names(list_of_pdfs)
        if os.path.isfile(files):
            list_of_pdfs = [files if files.endswith(".pdf") else None]
            print_names(list_of_pdfs)
    except:
        print("Incorrect specified filepath or directory!")
        exit()
    #
    # dir = "pub_phi_article/"
    # list_of_pdfs = [file for file in os.listdir(dir) if file.endswith(".pdf")]
    # for file in list_of_pdfs:
    #     filepath = dir + file
    #     doi_number = get_doi_number_from_pdf(filepath)
    #     if not doi_number: pass
    #     message = fetch_doi_message(doi_number)
    #     fn = construct_name(message)
    #     print("File name:\t\t{}".format(fn))
    #     print("____________________\n")
