# cook your dish here
import math
t = int(input())
for i in range(t):
    X, Y = map(int, input().split())
    diff = X - Y
    t = math.ceil((-1 + math.sqrt(1 + 8 * diff)) / 2)
    print(t)