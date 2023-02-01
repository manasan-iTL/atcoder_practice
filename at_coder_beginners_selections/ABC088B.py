n = int(input())
list_num = list(map(int, input().split()))

alice_num = 0
bob_num = 0

# list_numを大きい順にソートする
new_list = sorted(list_num, reverse=True)

# new_listをループし、奇数→Alice 偶数→Bob
for i, num in enumerate(new_list):
  if (i + 1) % 2 == 0:
    bob_num += num
  else:
    alice_num += num

print(alice_num - bob_num)