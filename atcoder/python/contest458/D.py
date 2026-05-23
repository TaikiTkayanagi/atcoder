import heapq

X = int(input())
Q = int(input())
ans = X
lower = []
higher = []

for _ in range(Q):
    A, B = map(int, input().split())

    if ans > A:
        heapq.heappush(lower, -A)
    else:
        heapq.heappush(higher, A)

    if ans > B:
        heapq.heappush(lower, -B)
    else:
        heapq.heappush(higher, B)

    while len(lower) != len(higher):
        if len(lower) > len(higher):
            tmp = -heapq.heappop(lower)
            heapq.heappush(higher, ans)
            ans = tmp
        else:
            tmp = heapq.heappop(higher)
            heapq.heappush(lower, -ans)
            ans = tmp
            
    print(ans)