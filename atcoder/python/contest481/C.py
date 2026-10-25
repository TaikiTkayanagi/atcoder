Q = int(input())

bank = {}
id = 1
for _ in range(Q):
    name = input()

    if name in bank:
        print(bank[name])
        continue

    print(id)
    bank[name] = id
    id += 1

    
