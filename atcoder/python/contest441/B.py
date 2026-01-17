N, M = map(int, input().split())
S = input()
T = input()
Q = int(input())

takahasi_map = set()
aoki_map = set()

for i in S:
    takahasi_map.add(i)
for i in T:
    aoki_map.add(i)

ans = []
for _ in range(0, Q):
    target = input()
    is_set = False
    for i in target:
        if i not in takahasi_map:
            ans.append("Aoki")
            is_set = True
            break
        if i not in aoki_map:
            ans.append("Takahashi")
            is_set = True
            break

    if not is_set:
        ans.append("Unknown")


for i in ans:
    print(i)
