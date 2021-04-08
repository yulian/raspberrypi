#  서울의 8월과 1월의 최고기온을 동시에 히스토그램으로 출력

import csv
import matplotlib.pyplot as plt
f = open('seoul.csv')
data = csv.reader(f)
header = next(data)
aug = []
jan = []
for row in data:
  if len(row)==5 and row[-1] != '':
    month = row[0].split('-')[1]
    if month == '08':
      aug.append(float(row[-1]))
    if month == '01':
      jan.append(float(row[-1]))
plt.hist(aug, bins=100, color='r')
plt.hist(jan, bins=100, color='b')
plt.show()
