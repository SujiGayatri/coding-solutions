# cook your dish here
t = int(input())
for i in range(t):
    X, Y, K = map(int, input().split())
    diff = abs(X - Y)
    if diff == K:
        print(0)
    elif abs(diff - K) % 2 == 0:
        print(abs(diff - K) // 2)
    else:
        print(-1)