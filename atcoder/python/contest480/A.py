S1 = input()
S2 = input()

a_index = -1
d_index = -1
for i, s in enumerate(S1):
    if s == 'A':
        a_index = i 
    if s == 'D':
        d_index = i

for i, s in enumerate(S2):
    if s== 'A':
        a_index = i + 2 
    if s== 'D':
        d_index = i + 2


if (a_index == 0 or a_index == 3) and (d_index == 0 or d_index == 3):
    print('No')
elif (a_index == 1 or a_index == 2) and (d_index == 1 or d_index == 2):
    print('No')
else:
    print('Yes')
