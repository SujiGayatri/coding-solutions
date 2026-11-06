# cook your dish here
t = int(input())
for i in range(t):
    N = int(input())
    if N % 3 == 0 or N % 4 == 0 or N >= 6:
        print("YES")
    else:
        print("NO")