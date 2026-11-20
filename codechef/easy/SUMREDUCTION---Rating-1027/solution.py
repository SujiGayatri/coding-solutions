# cook your dish here
t = int(input())
for u in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    while len(a) > 1:
        found = False

        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if (a[i] & a[j]) == 0:
                    s = a[i] + a[j]

                    a.pop(j)
                    a.pop(i)
                    a.append(s)

                    found = True
                    break

            if found:
                break

        if not found:
            break

    print("Yes" if len(a) == 1 else "No")