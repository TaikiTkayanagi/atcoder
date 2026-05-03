S = input()
L = len(S)

count = 0
i = 0
while L > i:
    s = S[i] 
    j = i + 1
    rate = 1
    while L > j:
        if s == S[j]:
            break 
        s = S[j]
        j += 1
        count += rate * 1
        rate += 1
    i = j

print((count + L) % 998244353)

        
        