h_list = [2, 9, 4, 5, 1, 6, 10]

cost = [0 for i in range(len(h_list))]
cost[0] = 0
cost[1] = abs(h_list[1] - h_list[0])

for i in range(2, len(h_list)):
    cost[i] = min(cost[i - 2] + abs(h_list[i - 2] - h_list[i]), cost[i - 1] + abs(h_list[i - 1] - h_list[i]))

print(cost[-1])
