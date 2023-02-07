n = int(input())
a = [list(map(int, input().split())) for l in range(n)]

# t2 - t1回で移動可能かどうかを判定すればよい
# 距離の算出→abs(x[i + 1] - x[i]) + abs(y[i + 1] - y[i]) 
# 上記の距離がt[i+1]-t[i]*1より小さいかどうか　