# cook your dish here
t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    total = sum(a)
    required = n * x
    ans = max(0, required - total)
    print(ans)