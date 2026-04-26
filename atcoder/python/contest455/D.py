N, Q = map(int, input().split())
class Node:
    def __init__(self, number, next=None, previous=None):
        self.number = number
        self.next = next
        self.previous = previous

card_map = [Node(i) for i in range(N)]
place_memo = [c for c in card_map]
for _ in range(Q):
    C, P = map(int, input().split())
    C -= 1
    P -= 1
    card_map[P].next = card_map[C]
    if card_map[C].previous != None:
        card_map[C].previous.next = None 
    card_map[C].previous = card_map[P]

    if place_memo[C] != None:
        place_memo[C] = None


for place in place_memo:
    ans = 0
    if place == None:
        print(ans, end=" ")
        continue

    iterator = place
    while iterator:
        iterator = iterator.next 
        ans += 1
    print(ans, end=' ')
        
        