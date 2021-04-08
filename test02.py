# 기상 관측 이래, 서울의 최저 기온이 가장 낮았던 날은 언제였고, 몇 도였을까?

import csv
min_temp = 100
mix_date = ''

f = open('seoul.csv', 'r')
data = csv.reader(f)
header = next(data)
for row in data:
  if len(row) != 5:
    continue
  if row[-2] == '':
    row[-2] = 100
  row[-2] = float(row[-2])
  if min_temp > row[-2]:
    min_date = row[0]
    min_temp = row[-2]
f.close()
print('Date:'+str(min_date)+', Temp:'+str(min_temp))
