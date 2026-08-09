N, Q = map(int, input().split())
P = list(map(int, input().split()))

for i in range(N):
    P[i] -= 1

P_R = [0] * N
for i,p in enumerate(P):
    P_R[p] = i

is_turn = False
for i in range(Q):
    inputs = input().split()
    query, x, y = map(int, inputs) if len(inputs) > 2 else (2, 0, 0)
    x -= 1
    y -= 1

    TARGET = P if not is_turn else P_R
    PLACE = P_R if not is_turn else P

    if query == 1:
        tmp_1 = TARGET[x]
        tmp_2 = TARGET[y]
        TARGET[x] = TARGET[y]
        TARGET[y] = tmp_1

        tmp_3 = PLACE[tmp_1]
        PLACE[tmp_1] = PLACE[tmp_2]
        PLACE[tmp_2] = tmp_3
    else:
        is_turn = not is_turn

ans = P if not is_turn else P_R

for a in ans:
    print(a+1, end=" ")