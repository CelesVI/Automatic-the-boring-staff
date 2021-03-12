import PyPDF2,os

os.chdir(r'C:\Users\Bravin\Desktop\Python\Automatic the boring stuff')
pdfFile = open(r'C:\Users\Bravin\Desktop\Python\Automatic the boring stuff\Historia del Cine.pdf', 'rb')
pdfFile2 = open(r'C:\Users\Bravin\Desktop\Python\Automatic the boring stuff\La Noche de los Museos.pdf', 'rb')

reader = PyPDF2.PdfFileReader(pdfFile)
reader2 = PyPDF2.PdfFileReader(pdfFile2)

print(reader.numPages)
page = reader.getPage(8)
for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())

writer = PyPDF2.PdfFileWriter()
for pageNum in range(reader.numPages):
    page = reader.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

outFile = open(r'Combine.pdf', 'wb')
writer.write(outFile)
outFile.close()
pdfFile.close()
pdfFile.close()

