# cook your dish here
t = int(input())
notes = [100, 50, 10, 5, 2, 1]
for i in range(t):
    n = int(input())
    count = 0
    for note in notes:
        count += n // note
        n %= note
    print(count)