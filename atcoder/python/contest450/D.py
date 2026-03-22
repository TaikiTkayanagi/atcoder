N, K = map(int, input().split())
A = list(map(int, input().split()))

mod_list = []
for a in A:
    mod_list.append(a % K)

mod_list = sorted(mod_list)

max_dis = 0
for i,m in enumerate(mod_list):
    if i == N-1:
        next = mod_list[0]
        max_dis = max(K - (m - next), max_dis)
    else:
        next = mod_list[i+1]
        max_dis = max(next - m, max_dis)

print(K - max_dis)