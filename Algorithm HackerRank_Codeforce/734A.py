n = int(input())
arr = list(map(str,input()))
D = 0
A = 0

for i in arr:
    if i == "D":
        D += 1
    elif i == "A":
        A += 1
    else:
        pass

if D > A:
    print("Danik")
elif A > D:
    print("Anton")
elif A == D:
    print("Friendship")
else:
    pass
