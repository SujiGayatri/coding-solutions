# cook your dish here
import math
T = int(input())
for i in range(T):
    B, LS = map(int, input().split())

    minimum = math.sqrt(LS * LS - B * B)
    maximum = math.sqrt(LS * LS + B * B)

    print(minimum, maximum)