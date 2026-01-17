P, Q = map(int, input().split())
X, Y = map(int, input().split())

ans = "Yes" if X >= P and P + 99 >= X and Y >= Q and Q + 99 >= Y else "No"

print(ans)
