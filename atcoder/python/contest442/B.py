Q = int(input())

volume = 0
is_music = False
for i in range(Q):
    A = int(input())

    if A == 1:
        volume += 1
    elif A == 2:
        if volume > 0:
            volume -= 1
    else:
        is_music = not is_music

    print('Yes' if is_music and volume >= 3 else 'No')
