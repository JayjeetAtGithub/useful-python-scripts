import PyPDF2 as pd
pdfFileObj = open('abcd.pdf','rb')
pdfReader = pd.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())
pdfFileObj.close()
