# cook your dish here
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    s = a + b
    if s < 3:
        print(1)
    elif s <= 10:
        print(2)
    elif s <= 60:
        print(3)
    else:
        print(4)
