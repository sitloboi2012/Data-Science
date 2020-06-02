n = int(input())
arr = list(map(int,input().split()))
arr.sort
highest = max(arr)
blow = 0

for i in arr:
    if i == highest:
        blow += 1
    else:
        pass

print(blow)
