# 우리 동네 인구 구조를 시각화해 인구수가 가장 많은 연령대와 가작 적은 연령대를 표시하자.

import csv
import matplotlib.pyplot as plt

f = open('age.csv', encoding='cp949')
data = csv.reader(f)
result = []
max = [-1, -1]
min = [-1, 1000000]
for row in data:
  if '1121500000' in row[0]:
    age = 0
    for i in row[3:]:
      ch = i.replace(',','')
      p = int(ch)
      if max[1]<p:
        max[0] = age
        max[1] = p
      if min[1]>p:
        min[0] = age
        min[1] = p
      age+=1
      result.append(p)

plt.title('Population of our neighborhood')
plt.plot(result, 'red')
plt.plot(max[0], max[1], 'b^', label=str(max[0]))
plt.plot(min[0], min[1], 'g^', label=str(min[0]))
plt.legend()
plt.show()
