#Get the highest numb in arr minus for the rest => get the rest of other a b c
#Lấy số lớn nhất trừ cho từng số trong arr sẽ ra được a b c

arr = list(map(int,input().split()))
largest = max(arr)

for i in arr:
    if largest - i > 0:
        print(largest - i, end = " ")



