n = int(input())
arr = list(map(str,input().split()))
total = 0

for i in range(len(arr)-1):
    if arr[i] == "U":
        total += 0
    elif arr[i] == "D" and arr[i+1] == "D" and arr[i-1] == "D":
        total += 0
    elif arr[i] == "D":
        if arr[i+1] == "D":
            total += 1
        else:
            total += 0
    else:
        pass






print(len(arr))

print(total)



