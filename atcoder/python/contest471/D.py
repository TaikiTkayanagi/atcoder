import heapq

Q, V = map(int, input().split())


heap = []
heapq.heapify(heap)
energy_list = []
for _ in range(Q):
    i = input().split()
    q, t, w = map(int, i)  if len(i) == 3 else (int(i[0]), int(i[1]), None)

    if q == 1:
        heapq.heappush(heap, (w - t) * -1)
        continue
    if q == 2:
        if len(heap) == 0:
            print(-1)
            continue
        v = heapq.heappop(heap) * -1 
        print(min(v + t, V))