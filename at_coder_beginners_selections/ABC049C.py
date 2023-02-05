s = input()
t = ["dream","dreamer","erase","eraser"]

# 後ろから単語を切り取っていけば良い


while s:
  isRest = True
  for word in t:
    if s.endswith(word):
      s = s[:len(s) - len(word)]
      isRest = False
      break
  if isRest:
    break

if s == "":
  print("YES")
else:
  print("NO")