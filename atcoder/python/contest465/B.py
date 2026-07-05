X, Y, L, R, A, B = map(int, input().split())

ans = 0
for i in range(A + 1, B+1):
    if i > L and i <= R:
        ans += X
    else:
        ans += Y 


print(ans)
         