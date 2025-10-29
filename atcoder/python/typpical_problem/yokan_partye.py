import math

N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

left = 0
right = L
while right - left > 1:
    mid = (left + right) // 2

    position = 0
    clear_size = 0
    for a in A:
        if a - position >= mid:
            position = a
            clear_size += 1
    if L - position >= mid:
        clear_size += 1

    if clear_size >= K + 1:
        left = mid
    else:
        right = mid
print(left)
