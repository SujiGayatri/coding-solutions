# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    if n == 2:
        count = 0
        for i in range(n):
            num = int(s[(i-1) % n] + s[i])
            if num % 4 == 0:
                count += 1
    else:
        count = 0
        for i in range(n):
            num = int(s[(i-2) % n] + s[(i-1) % n])
            if num % 4 == 0:
                count += 1
    print(count)