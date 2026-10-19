# cook your dish here
t = int(input())
for i in range(t):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = min(A[N - 1] - A[1], A[N - 2] - A[0])
    print(ans)