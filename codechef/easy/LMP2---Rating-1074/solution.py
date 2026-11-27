# cook your dish here
from collections import Counter
t = int(input())
for i in range(t):
    n = int(input())
    s = input()

    freq = Counter(s)

    if max(freq.values()) > 2:
        print("NO")
    else:
        print("YES")