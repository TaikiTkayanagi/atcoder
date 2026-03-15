N = int(input())

S = []
max = 0
for _ in range(N):
    s = input()
    S.append(s)
    max = max if max > len(s) else len(s)


answer = []
for i in range(N):
    l = len(S[i])
    if max == l:
        answer.append(S[i])
        continue
    d = max - l
    a = ""
    for _ in range(d//2):
        a += "."
    a += S[i]
    for _ in range(d//2):
        a += "."
    answer.append(a)

for a in answer:
    print(a)
