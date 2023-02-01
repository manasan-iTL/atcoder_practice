n = int(input())
num_mochi = [int(input()) for i in range(n)]

new_num_mochi = sorted(num_mochi, reverse=True)

# 配列の要素で値が同じ要素を削除する
no_duplication_mochi = []

# 自前実装の場合、前の要素と同じかを判定する→not in演算子で代用
for num in new_num_mochi:
  if num not in no_duplication_mochi:
    no_duplication_mochi.append(num)

print(len(no_duplication_mochi))