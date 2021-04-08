# 특정한날에 대한 최고, 최저기온을 그래프로 출력

import csv
import matplotlib.pyplot as plt
f = open('seoul.csv')
data = csv.reader(f)
next(data)
high = []
low = []
for row in data:
  if len(row) != 5:
    continue
  if len(row[-1])>0 and len(row[-2])>0:
    date = row[0].split('-')
    if 2000 <= int(date[0]):
      if date[1] == '01' and date[2] == '01':
        high.append(float(row[-1]))
        low.append(float(row[-2]))
plt.title("Graph for my birthday's temperature changes")
plt.plot(high, 'hotpink', label='high')
plt.plot(low, 'skyblue', label='low')
plt.legend()
plt.show()
