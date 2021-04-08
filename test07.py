# 우리동네 인구 구조를 바차트로 출력

import csv
import matplotlib.pyplot as plt

f = open('age.csv', encoding='cp949')
data = csv.reader(f)
result = []

for row in data:
  if '1121500000' in row[0]:
    for i in row[3:]:
      ch = i.replace(',','')
      result.append(int(ch))

plt.title('Population of our neighborhood')
plt.bar(range(101), result)
plt.show()

