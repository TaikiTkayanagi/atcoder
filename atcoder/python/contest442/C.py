N, M = map(int, input().split())
count = [0] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    count[A] = count[A] + 1
    count[B] = count[B] + 1


for i in range(1, N + 1):
    S = N - 1 - count[i]

    if 3 > S:
        print(0, end=" ")
        continue

    ans = (S * (S - 1) * (S - 2)) // 6
    print(ans, end=" ")
