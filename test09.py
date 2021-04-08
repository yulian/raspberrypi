# 지역명을 입력하면 인구 구조를 그래프로 출력

import csv
import matplotlib.pyplot as plt

f = open('age.csv', encoding='cp949')
data = csv.reader(f)
result = []
zone = input('지역명을 입력하세요 : ')

for row in data:
  if zone in row[0]:
    for item in row[3:]:
      item = item.replace(',','')
      result.append(int(item))
    break
else:
  print("검색하는 지역이 없습니다.")

plt.title('Population of our neighborhood')
plt.barh(range(101), result)
plt.show()

