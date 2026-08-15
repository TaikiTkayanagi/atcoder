N = int(input())
A = list(map(int, input().split()))
plus_A = []
minus_A = []

for a in A:
    if a > 0:
        plus_A.append(a)
    else:
        minus_A.append(a)

plus_A.sort()
minus_A.sort()
minus_A.reverse()
    
plus_A_index = 0
minus_A_index = 0

c = 0
ans = 0
while plus_A_index < len(plus_A) or minus_A_index < len(minus_A):
    p = abs(c - plus_A[plus_A_index]) if plus_A_index < len(plus_A) else -1
    m = abs(c - minus_A[minus_A_index]) if minus_A_index < len(minus_A) else -1


    if p == -1 or (m != -1 and p >= m):
        ans += m
        c = minus_A[minus_A_index]
        minus_A_index += 1
    else:
        ans += p
        c = plus_A[plus_A_index]
        plus_A_index += 1
        
        
print(ans) 