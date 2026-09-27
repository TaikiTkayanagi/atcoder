Q = int(input())
S = input()
T = input()

q = []
for n in range(Q):
    L, R = map(int, input().split())
    L -= 1
    R -= 1
    t = [0] * 3
    t[0] = n 
    t[1] = L
    t[2] = R
    q.append(t)

q = sorted(q, key=lambda x:x[1])
q_index = 0

i = 0
ans = ['No'] * Q
while i + (len(T)-1) < len(S):
    if S[i] != T[0]:
        i += 1
        continue
    
    is_ok = True
    i_2 = i
    for j in range(len(T)):
        if S[i_2] == T[j]:
            i_2 += 1
        else:
            is_ok = False
            break
        
    if is_ok:
        loop_count = 0
        for k in range(q_index, Q):
            n ,l, r = q[k]
            if l > i:
                break
            if i_2 - 1 <= r:
                ans[n] = 'Yes'
            loop_count += 1
        q_index += loop_count
    i += 1

                 
for a in ans:
    print(a)