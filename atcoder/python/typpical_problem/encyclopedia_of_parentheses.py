from collections import deque
from typing import Union

N = int(input())
START_PARETHESES = "("
END_PARETHESES = ")"

my_dequeu: deque[dict[str, Union[str, int]]] = deque()

my_dequeu.append({"s": START_PARETHESES, "c": 1})

ans = []
while my_dequeu:
    pop = my_dequeu.popleft()
    s = pop.get("s")
    c = pop.get("c")

    if N == 1:
        continue
    if c < 0:
        continue

    if len(s) == N:
        if c == 0:
            ans.append(s)
        continue

    my_dequeu.append({"s": s + START_PARETHESES, "c": c + 1})
    my_dequeu.append({"s": s + END_PARETHESES, "c": c - 1})

for a in ans:
    print(a)
