N,M = map(int, input().split())


memo = {}
for _ in range(M):
    A,B = map(int, input().split())

    if A in memo:
        memo[A].append(B)
    else:
        memo[A] = [B]

queue = [1]
duplicate = {1}
ans = 0
while queue:
    pop = queue.pop()
    if pop in memo:
        next = memo[pop]
        for v in next:
            if v in duplicate:
                continue
            queue.append(v)
            duplicate.add(v)
    ans += 1

print(ans)