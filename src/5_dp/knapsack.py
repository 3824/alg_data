import math

value = [3,2,6,1,3,85]
weight = [2,1,3,2,1,5]
w_limit = 11

dp = [[-math.inf] * (w_limit+1) for i in range(len(value)+1)]
for i in range(w_limit+1):
    dp[0][i] = 0
for i in range(len(value)+1):
    dp[i][0] = 0

## 縦が選択したアイテム数、横がその時点の重さ
for i in range(len(value)):
    for j in range(w_limit):
        # j is the weight at this point.
        # case of selecting the current item.
        if j + weight[i] <= w_limit:
            dp[i+1][j + weight[i]] = max(dp[i+1][j + weight[i]], dp[i][j] + value[i])
        # case of not selecting the current item.
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])

print(dp[len(value)][w_limit])

