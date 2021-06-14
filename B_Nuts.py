N = int(input())

A_n = list(map(int, input().split()))
result = 0

for i in range(N):
    # 10より大きい場合は
    while(A_n[i] > 10):
        A_n[i] -= 1
        result += 1


print(result)