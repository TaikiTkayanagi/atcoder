S = input()
L = len(S)

count = 0
dp = {'a': 0, 'b': 0, 'c': 0}
for s in S:
    dp[s] = (dp['a'] + dp['b'] + dp['c'] + 1) % 998244353

for d in dp.values():
    count += d
    
   
        

print(count % 998244353)