# cook your dish here
t = int(input())
for i in range(t):
    n = input().strip()
    if n == n[::-1]:
        print("wins")
    else:
        print("loses")