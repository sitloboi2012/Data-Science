n = input()
arr = list(map(int,input().split()))
total = 0

for i in range(len(arr) - 1):
    while arr[i] == 0:
        if arr[i + 1] == 0:
            total += 1
            if arr[i + 2] == 0:
                total += 0
            else:
                pass
        elif arr[i + 1] == 1 and arr[i + 2] == 0:
            total += 1
        else:
            pass
        break 
    else:
        total += 0
        pass


print(total)
