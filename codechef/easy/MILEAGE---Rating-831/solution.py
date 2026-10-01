# cook your dish here
t = int(input())
for i in range(t):
    N, X, Y, A, B = map(int, input().split())
    petrol_cost = X * B
    diesel_cost = Y * A
    if petrol_cost < diesel_cost:
        print("PETROL")
    elif petrol_cost > diesel_cost:
        print("DIESEL")
    else:
        print("ANY")