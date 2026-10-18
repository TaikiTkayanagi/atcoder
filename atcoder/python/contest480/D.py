from bisect import bisect_right

N, Q = map(int, input().split())
A = list(map(int, input().split()))

S = [0]
P = [0]
ends = [0]

for i in range(1, N + 1):
    S.append(S[-1] + A[i - 1])
    P.append(P[-1] + S[i])
    ends.append(ends[-1] + i)

def f(x):
    k = bisect_right(ends, x) - 1
    rest = x - ends[k]
    return P[k] + S[rest]

for _ in range(Q):
    L, R = map(int, input().split())
    print(f(R) - f(L - 1))