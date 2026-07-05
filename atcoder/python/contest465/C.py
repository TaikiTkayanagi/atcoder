N = int(input())
S = input()

A = [0] * N

left = 0
right = N-1
is_reverse = False
for i in range(N-1, -1, -1):
    if not is_reverse and S[i] == 'o':
        A[left] = i + 1
        left += 1
        is_reverse = True
    elif is_reverse and S[i] == 'x':
        A[left] = i + 1
        left += 1
    elif not is_reverse and S[i] == 'x':
        A[right] = i + 1
        right -= 1
    else:
        A[right] = i + 1
        right -= 1
        is_reverse = False
        

for a in A:
    print(a, end=' ')