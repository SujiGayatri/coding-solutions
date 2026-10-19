# cook your dish here
t = int(input())
for i in range(t):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    total = sum(A)
    min_loss = min(A[i] - B[i] for i in range(N))
    print(total - min_loss)