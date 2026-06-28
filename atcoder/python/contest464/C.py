N, M = map(int, input().split())

count = set()
diff = [0] * M
state = {}
d_list = []
for _ in range(N):
    A, D, B = map(int, input().split())
    count.add(A)
    d_list.append([A, D, B])
    if A in state:
        state[A] += 1
    else:
        state[A] = 1

d_list = sorted(d_list, key=lambda d: d[1])

for d in d_list: 
    A, D, B = map(int, d)
    if B in state:
        state[B] += 1
    else:
        state[B] = 1
    state[A] -= 1

    if A == B:
        continue

    if state[A] == 0 and state[B] > 1:
        diff[D-1] -= 1
    elif state[A] > 0 and state[B] == 1:
        diff[D - 1] += 1

ans = len(count)
for i in range(M):
    ans += diff[i]
    print(ans)