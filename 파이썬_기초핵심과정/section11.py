# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV File : MIME - text/csv 형식 몰라~~ 뭐라카노~
# Comma Separate Value

import csv

with open('./resource/sample1.csv','r') as f:
    reader = csv.reader(f)

    print(reader)
    print(type(reader))
    print(dir(reader))
    print('')

    for c in reader:
        print(c)

    

with open('./resource/sample2.csv','r') as f:
    reader = csv.reader(f, delimiter = '|') 

    print(reader)
    print(type(reader))
    print(dir(reader))
    print('')

    for c in reader:
        print(c)



with open('./resource/sample1.csv','r') as f:
    reader = csv.DictReader(f)

    for c in reader:
        for k, v in enumerate(c.items()):
            if k == 3 :
                print(v[0],end =" ")
                print(v[1])


w = [[1,2,3],[4,5,6],[7,8,9],[0,0,0]]
# with open('./resource/sampe3.csv', 'w', newline="") as f:
#     wt = csv.writer(f)
#     for v in w:
#         wt.writerow(v)

with open('./resource/sampe3.csv', 'w', newline="") as f:
    wt = csv.writer(f)
    wt.writerows(w) # for문 대용


# XSL, XLSX
# openpyxl, xlsxwriter, xlrd, xlwt, xlutils
# pandas를 주로 사용 (openpyxl, xlrd) 만능
# pip install xlrd
# pip install openpyxl
# pip install pandas

import pandas 

# sheetname = 이름 또는 숫자로,
# header = 숫자
# skiprow = 숫자
xlsx = pandas.read_excel('./resource/sample.xlsx',)
print(xlsx.head())
print('')
print(xlsx.tail())

print(xlsx.shape)