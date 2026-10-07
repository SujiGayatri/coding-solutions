# cook your dish here
t = int(input())
for i in range(t):
    salary = int(input())
    if salary < 1500:
        hra = 0.10 * salary
        da = 0.90 * salary
    else:
        hra = 500
        da = 0.98 * salary

    gross = salary + hra + da

    print(f"{gross:.2f}")