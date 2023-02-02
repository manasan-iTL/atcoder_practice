n, y = list(map(int, input().split()))

# 存在するペアを保存
pair_number = []

# 全探索してみる→計算量がオーバーする。１０００園に関してループしなくても枚数が確定するため、２重ループで十分


for i in range(n + 1):
  for j in range(n + 1):
    if n - (i + j) < 0:
      c = n
    else:
      c = n - (i + j)
    if (10000*i + 5000*j + 1000*c == y) and (i + j + c == n):
      pair_number.append({"x": i, "y": j, "z": c})

if len(pair_number) > 0:
  print(pair_number[0]["x"], pair_number[0]["y"], pair_number[0]["z"])
else:
  print(-1, -1, -1)