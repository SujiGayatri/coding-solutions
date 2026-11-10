# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = float('inf')
    for i in range(n - 1):
        ans = min(ans, arr[i] + arr[i + 1])
    print(ans)