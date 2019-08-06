import PyPDF2

# rb is read only format

file = open('C:\\Users\\Nxt\\PycharmProjects\\PythonSeleniumsessions\\PDF file\\ST market  Trends.pdf', 'rb')
pdfreader = PyPDF2.PdfFileReader(file)
print(pdfreader.getNumPages())

# from starting page
pageobj = pdfreader.getPage(0)
print(pageobj.extractText())
file.close()

