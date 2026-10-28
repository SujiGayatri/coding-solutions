# cook your dish here
t = int(input())

for o in range(t):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    left = 0
    right = N - 1
    possible = True

    while left < right:
        if A[left] == A[right]:
            left += 1
            right -= 1

        elif A[left] == K:
            left += 1

        elif A[right] == K:
            right -= 1

        else:
            possible = False
            break

    print("Yes" if possible else "No")