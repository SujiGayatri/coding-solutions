# cook your dish here
t = int(input())
for i in range(t):
    N, M = map(int, input().split())
    if N % 2 == 0 or M % 2 == 0:
        print("Yes")
    else:
        print("No")