# 기상 관측 이래, 서울의 최고 기온이 가장 높았던 날은 언제였고, 몇 도였을까?

import csv
max_temp = -100
max_date = ''

f = open('seoul.csv', 'r')

data = csv.reader(f)
header = next(data)
for row in data:
  if len(row) != 5:
    continue
  if row[-1] == '':
    row[-1] = -100
  row[-1] = float(row[-1])
  if max_temp < row[-1]:
    max_date = row[0]
    max_temp = row[-1]

f.close()
print('Date:'+str(max_date)+', Temp:'+str(max_temp))
