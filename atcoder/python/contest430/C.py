N, A, B = map(int, input().split())
S = input()

right = 0
left = 0
a_counter = 0
b_counter = 0
ans = 0
while (N > right):
    if S[right] == "a":
        a_counter += 1
    else:
        b_counter += 1

    if b_counter >= B:
        if S[left] == "a":
            a_counter -= 1
        else:
            b_counter -= 1
        left += 1
    elif a_counter >= A:
        print("left: " + str(left) + "right: " + str(right))
        while a_counter >= A:
            ans += 1
            if S[left] == "a":
                a_counter -= 1
            else:
                b_counter -= 1
            left += 1

    right += 1

print(ans)
