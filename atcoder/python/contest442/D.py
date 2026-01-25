N, Q = map(int, input().split())
A = list(map(int, input().split()))

counter = [0] * N
for i in range(N):
    counter[i] = counter[i-1] + A[i]


for _ in range(Q):
    q, *v = map(int, input().split())
    if q == 1:
        index = v[0] - 1
        tmp = A[index]
        A[index] = A[index+1]
        A[index+1] = tmp
        counter[index] = A[index] if index == 0 else A[index] + \
            counter[index - 1]

    else:
        start = v[0] - 1
        end = v[1] - 1

        if start == 0:
            print(counter[end])
        else:
            ans = counter[end] - counter[start - 1]
            print(ans)
