# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    s = input()

    count = 0
    i = 0

    while i < n - 2:
        if s[i] == s[i + 1] == s[i + 2]:
            count += 1
            i += 3
        else:
            i += 1

    print(count)