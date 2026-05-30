X = int(input())
v2 = 'HelloWorld'
ans = ''
for i, v in enumerate(v2):
    if i+1 == X:
        continue 
    ans += v
print(ans)