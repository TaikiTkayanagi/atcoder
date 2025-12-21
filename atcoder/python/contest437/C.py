T = int(input())
ans_list = []

for _ in range(T):

    N = int(input())

    costs = []
    s = 0
    for _ in range(N):
        w, p = map(int, input().split())
        costs.append(w + p)
        s += p

    costs.sort()

    ans = 0
    total = 0
    for cost in costs:
        if total + cost <= s:
            ans += 1
            total += cost

    ans_list.append(ans)

for ans in ans_list:
    print(ans)
