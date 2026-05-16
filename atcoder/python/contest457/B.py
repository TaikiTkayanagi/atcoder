N = int(input())
L = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    L.append(tmp[1:])
X, Y = map(int, input().split())

print(L[X-1][Y-1])