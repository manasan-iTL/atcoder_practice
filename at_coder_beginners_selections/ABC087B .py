yen500 = int(input())
yen100 = int(input())
yen50 = int(input())
total_yen = int(input())

count = 0
# 全通り調べる→３重ループ(全探索)
# range範囲はプラス１→0枚を考慮するため

for i in range(yen500 + 1):
  for j in range(yen100 + 1):
    for k in range(yen50 + 1):
      if (500*i + 100*j + 50*k == total_yen):
        count += 1
print(count)