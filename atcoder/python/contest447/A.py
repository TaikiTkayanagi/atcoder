N, M = map(int, input().split())

answer = "Yes"
count = 0
for i in range(0, N, 2):
    count += 1

print("Yes" if count >= M else "No")

