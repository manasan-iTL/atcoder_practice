N = int(input())

num_list = list(map(int, input().split()))

# 毎回の条件は偶数かどうか
# 偶数の場合→すべて割り、値を更新

flag = False
count = 0

while True:
  for i, num in enumerate(num_list):
    if num % 2 == 1:
      flag = True
    else:
      num_list[i] = num // 2
      
  if flag:
    break
  count += 1
    
print(count)