# cook your dish here
t = int(input())
for i in range(t):
    days = list(map(int, input().split()))
    sunny = sum(days)
    if sunny > 3:
        print("YES")
    else:
        print("NO")