N = int(input())


left = 1
ans = 0
for i in range(1, N):
    right = max(i+1, left+1)

    count = right - i - 1
    while N + 1 > right:
        print(f'? {i} {right}')

        if input() == 'Yes':
            count = right - i
            left = right
            right += 1
        else:
            break
    ans += count

print(f'! {ans}')
