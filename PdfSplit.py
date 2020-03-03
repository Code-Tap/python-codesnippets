#! /usr/bin/python3

from PyPDF2 import PdfFileWriter, PdfFileReader
from multiprocessing import Pool
import glob, sys, os

pdfs = glob.glob("/mnt/usb_1/scans/*.pdf")

def process_pdfs(pdf):
    path, target = os.path.split(pdf)
    inputpdf = PdfFileReader(open(path + "/" + target , "rb"))
    print("Processing %s"% target)
    for i in range(inputpdf.numPages // 2):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i * 2))

        if i * 2 + 1 <  inputpdf.numPages:
            output.addPage(inputpdf.getPage(i * 2 + 1))

        newname = path + "/" + "processed" + "/" + target[:-4] + "-" + str(i) + ".pdf"

        outputStream = open(newname, "wb")
        output.write(outputStream)
        outputStream.close()

p = Pool(processes=4)
p.map(process_pdfs, pdfs)
