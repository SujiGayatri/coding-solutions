# cook your dish here
t = int(input())
for i in range(t):
    A, B, C = map(int, input().split())

    if A + B == C:
        print("YES")
    else:
        print("NO")