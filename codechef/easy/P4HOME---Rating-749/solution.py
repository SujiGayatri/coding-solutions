# cook your dish here
t = int(input())
for i in range(t):
    x, y, z = map(int, input().split())
    ans = 2 * min(y, z)
    print(ans)
