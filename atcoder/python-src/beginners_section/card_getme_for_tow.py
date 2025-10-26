n = int(input())
a = list(map(int, input().split()))
a.sort()

alice = 0
bob = 0
isAlice = True
for x in reversed(a):
    if isAlice:
        alice += x
        isAlice = False
    else:
        bob += x
        isAlice = True

print(alice - bob)
