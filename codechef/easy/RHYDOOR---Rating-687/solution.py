# cook your dish here
t = int(input())
for i in range(t):
    N = int(input())
    S = input().strip()
    count = 0
    consecutive = 0
    prev = ''
    for ch in S:
        if ch == prev:
            consecutive += 1
        else:
            consecutive = 1
            prev = ch
        if consecutive == 3:
            count += 1
            consecutive = 0

    print(count)