A = []

for _ in range(3):
    A.append(list(map(int, input().split())))

count = 0
for a1 in A[0]:
    for a2 in A[1]:
        for a3 in A[2]:
            if a1 == 4 and a2 == 5 and a3 == 6:
                count += 1
            elif a1 == 5 and a2 == 6 and a3 == 4:
                count += 1
            elif a1 == 5 and a2 == 4 and a3 == 6:
                count += 1
            elif a1 == 6 and a2 == 4 and a3 == 5:
                count += 1
            elif a1 == 6 and a2 == 5 and a3 == 4:
                count += 1
            elif a1 == 4 and a2 == 6 and a3 == 5:
                count += 1
                
print(count / 216)