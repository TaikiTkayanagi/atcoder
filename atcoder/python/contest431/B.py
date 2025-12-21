X = int(input())
N = int(input())
W = list(map(int, input().split()))
Q = int(input())
P = []
for i in range(Q):
    P.append(int(input()))

memo = set()
ans = X
for v in P:
    v = v - 1
    if v in memo:
        memo.remove(v)
        ans = ans - W[v]
    else:
        memo.add(v)
        ans = ans + W[v]
    print(ans)
