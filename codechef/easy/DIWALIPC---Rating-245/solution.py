# cook your dish here
t = int(input())
for i in range(t):
    p, d, k, b = map(int, input().split())
    total = p + (d * k)
    if total <= b:
        print("YES")
    else:
        print("NO")