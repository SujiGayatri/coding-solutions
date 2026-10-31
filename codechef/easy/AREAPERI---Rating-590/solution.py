# cook your dish here
L = int(input())
B = int(input())
area = L * B
perimeter = 2 * (L + B)
if area > perimeter:
    print("Area")
    print(area)
elif perimeter > area:
    print("Peri")
    print(perimeter)
else:
    print("Eq")
    print(area)