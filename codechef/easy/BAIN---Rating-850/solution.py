# cook your dish here
a, b, c, d = map(int, input().split())
arr = [a, b, c, d]
found = False
for i in range(1, 16):
    total = 0
    for j in range(4):
        if i & (1 << j):
            total += arr[j]
    if total == 0:
        found = True
        break
print("Yes" if found else "No")
