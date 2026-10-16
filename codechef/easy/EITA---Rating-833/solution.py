# cook your dish here
t = int(input())
for i in range(t):
    d, x, y, z = map(int, input().split())
    strategy1 = 7 * x
    strategy2 = d * y + (7 - d) * z
    print(max(strategy1, strategy2))