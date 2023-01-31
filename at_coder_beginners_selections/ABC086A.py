num_a, num_b = list(map(int, input().split()))

if (num_a * num_b % 2 == 0):
  print("Even")
else:
  print("Odd")