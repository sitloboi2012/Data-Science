n = int(input())
arr = list(map(int,input().split()))
arr.sort()
total = 0

def sockMerchant(n,arr):
    count = 0
    arr.append("#")
    i = 0
    while i < n:
        if arr[i]==arr[i+1]:
            count = count+1
            i+=2
        else:
            i+=1
    return count



result = sockMerchant(n,arr)
print(result)
