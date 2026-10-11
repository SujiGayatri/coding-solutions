# cook your dish here
t = int(input())
for i in range(t):
    N = int(input())
    attA = list(map(int, input().split()))
    defA = list(map(int, input().split()))
    attP = list(map(int, input().split()))
    defP = list(map(int, input().split()))
    total_att_A = sum(attA)
    total_def_A = sum(defA)
    total_att_P = sum(attP)
    total_def_P = sum(defP)

    if total_att_A > total_att_P and total_def_A > total_def_P:
        print("A")
    elif total_att_P > total_att_A and total_def_P > total_def_A:
        print("P")
    else:
        print("DRAW")