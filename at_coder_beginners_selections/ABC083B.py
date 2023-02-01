n,a,b = list(map(int, input().split()))

num_total = 0
# 1 <= num <= nの整数 かつ 各桁の和がa <= num <= b

for num in range(n + 1):
  sum_digit = 0
  flag = False
  for i, size_num in enumerate(str(num)):
    sum_digit += int(size_num)
    if i == len(str(num)) - 1 and (a <= sum_digit <= b):
      flag = True
  if flag:
  	num_total += int(num)

print(num_total)