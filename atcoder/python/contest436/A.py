N = int(input())
S = input()

d = N - len(S)

r = ""
for i in range(d):
    r += "o"

print(r + S)
