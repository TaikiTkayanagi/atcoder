N, D = map(int, input().split())
X = list(map(int, input().split()))
ans = 0
ans_list = []
for i in range(N):
    ok = True
    for j in range(N):
        if i == j:
            continue

        if abs(X[i] - X[j]) < D:
            ok = False
            break
            
    if ok:
        ans += 1
        ans_list.append(i+1)


print(ans)
if len(ans_list) == 0:
    print()
else:
    for a in ans_list:
        print(a, end=" ")