# cook your dish here
t = int(input())
for i in range(t):
    X, Y = map(int, input().split())
    print(2 * max(X, Y) - 1)