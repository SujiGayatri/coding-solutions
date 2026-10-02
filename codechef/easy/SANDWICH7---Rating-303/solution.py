# cook your dish here
import sys

def solve():
    B, H, C = map(int, sys.stdin.read().split())
    bread_limit = B // 2
    filling_limit = H + C
    print(min(bread_limit, filling_limit))

if __name__ == "__main__":
    solve()