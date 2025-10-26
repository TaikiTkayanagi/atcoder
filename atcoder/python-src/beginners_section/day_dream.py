S = input()


s = len(S)
for i in reversed(range(len(S))):
    if s - i < 5:
        continue
    c = S[i:s]
    if c == "erase":
        s = i
    elif c == "dream":
        s = i
    elif c == "dreamer":
        s = i
    elif c == "eraser":
        s = i

print("YES" if s == 0 else "NO")
