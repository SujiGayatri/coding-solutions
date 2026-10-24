# cook your dish here
t = int(input())
for i in range(t):
    X, Y, Z = map(int, input().split())
    ans = min(X, Z) + Y // 2
    print(ans)