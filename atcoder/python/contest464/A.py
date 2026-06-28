S = input()

e = 0
w = 0
for s in S:
    if s == 'E':
        e += 1
    else: 
        w += 1

print('East' if e > w else 'West') 