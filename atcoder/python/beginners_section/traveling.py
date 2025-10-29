n = int(input())
travle = []
for i in range(n):
    l = list(map(int, input().split()))
    travle.append(l)

current_x = 0
current_y = 0
timer = 0
travel_index = 0
while travel_index < len(travle):
    timer += 1
    t, x, y = travle[travel_index]
    if current_x != x:
        current_x = current_x + 1 if x > current_x else current_x - 1
    else:
        current_y = current_y + 1 if y > current_y else current_y - 1

    if timer == t and current_x == x and current_y == y:
        travel_index += 1
    elif timer >= t:
        print("No")
        exit(0)

print("Yes")
