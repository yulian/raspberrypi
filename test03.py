import csv
f = open('seoul.csv', 'r')
data = csv.reader(f)
header = next(data)
day = input('날짜를 입력하세요 ex)2020-01-01 : ')
for row in data:
  if len(row) == 5 and day == row[0]:
    print('최고온도:'+str(row[-1])+' 최저온도:'+str(row[-2]))
