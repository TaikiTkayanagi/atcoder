N, K = map(int, input().split())

loop = 0
count = 0
while K > count:
    count += (N + loop)
    loop += 1

print(loop - 1)
