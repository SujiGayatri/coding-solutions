# cook your dish here
t = int(input())
for i in range(t):
    N, M = map(int, input().split())
    S = input().strip()
    L = input().strip()
    left = set(L)
    current = 0
    maximum = 0
    previous_hand = None
    for ch in S:
        hand = 'L' if ch in left else 'R'
        if hand == previous_hand:
            current += 1
        else:
            current = 1
            previous_hand = hand
        maximum = max(maximum, current)
    print(maximum)