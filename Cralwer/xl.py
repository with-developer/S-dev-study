import openpyxl

book = openpyxl.Workbook()

sheet = book.active
sheet.append([1,2,3,4,5])

book.save("result.xlsx")
book.close()