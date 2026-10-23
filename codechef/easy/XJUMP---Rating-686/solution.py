# cook your dish here
t = int(input())
for i in range(t):
    X, Y = map(int, input().split())
    ans = X // Y + X % Y
    print(ans)