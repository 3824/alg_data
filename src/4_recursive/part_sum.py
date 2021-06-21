N = 10 # 整数の数
W = 55 # 探索する整数値
# 要素数がN個の整数値リストを作る。
num_list = [i+1 for i in range(N)]

def search_rec(n_list, sum):
    if len(n_list) == 0:
        return sum == 0
    num = n_list[0]
    return search_rec(n_list[1:], sum) or search_rec(n_list[1:], sum-num)

if __name__ == '__main__':
    print(search_rec(num_list, W))
