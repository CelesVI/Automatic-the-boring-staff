import openpyxl, os
os.chdir(r'C:\Users\Bravin\Desktop\Python\Automatic the boring stuff')

workbook = openpyxl.load_workbook('fruits.xlsx')
print(type(workbook))
sheet = workbook.get_sheet_by_name('Hoja1')
print(type(sheet))
print(workbook.get_sheet_names())
cell = sheet['A1']
print(cell.value)
print(sheet['B1'].value)
print(sheet['C1'].value)
for i in range(1,8):
    print(i, sheet.cell(row=i, column=2).value)
