N = input()

iterator = N
ret = "Yes"
memo = set()
memo.add(iterator)
while iterator != '1':
    total = 0
    for i in iterator:
        total += int(i) ** 2
    iterator = str(total)
    if iterator in memo:
        ret = "No"
        break
    memo.add(iterator)

print(ret)
