import xlrd
import xlwt

# 打开文件
workbook = xlrd.open_workbook('data.xls')
sheet = workbook.sheet_by_index(0)
count_data = []
percentage_data = []

row = 32
count_columns = [1, 3, 5, 7, 9, 12, 14, 16, 18, 20, 23, 25, 27, 29, 31]
percentage_columns = [2, 4, 6, 8, 10, 13, 15, 17, 19, 21, 24, 26, 28, 30, 32]

for column in count_columns:
    a = int(sheet.cell(row, column).value)
    count_data.append(a)

for column in percentage_columns:
    percentage_data.append(sheet.cell(row, column).value)

print(count_data)
print(percentage_data)
