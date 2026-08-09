N, Q = map(int, input().split())


A = [0] * N
ans = 0
idxs = set()
for i in range(Q):
    inputs = input().split()
    query, index = map(int, inputs) if len(inputs) > 1 else (int(inputs[0]), 0) 

    if query == 1:
        before = A[index-1]
        ans ^= before
        A[index-1] += 1
        ans ^= A[index-1]
        idxs.add(index-1)
    else:
        new_idxs = set()
        for i in idxs:
            if A[i] >= 1:
                before = A[i]
                ans ^= before
                A[i] -= 1
                ans ^= A[i]
                if A[i] > 0:
                    new_idxs.add(i)
        
        idxs = new_idxs

        
    print(ans)
        


        
