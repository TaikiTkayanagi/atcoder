N = int(input())

c_list = []
for i in range(N - 1):
    c_list.append(list(map(int, input().split())))
    
answer = "No"
is_ok = False
for i in range(N - 2):
    for j in range(i+1, N - 1):
        for k in range(j+1, N): 
            a1 = c_list[i][k - i - 1]
            a2 = c_list[i][j- i - 1] + c_list[j][k - j - 1]

            if a1 > a2:
                answer = "Yes"
                is_ok = True
                break
        if is_ok:
            break
    if is_ok:
        break

print(answer)
                

