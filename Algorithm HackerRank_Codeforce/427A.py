#Probelm 427A.py
#Description:
#Given the chronological order of crime occurrences and recruit hirings, find the number of crimes which will go untreated

#Với mỗi -1 thì crime + 1
#Với mỗi 1 thì police + 1. Nếu police + 1 thì crime - 1
#In cái số crime còn lại
#Nếu crime xảy ra trước police thì không tính

n = int(input())
arr = list(map(int,input().split()))
crime = 0
police = 0


for i in range(len(arr)-1):
    for j in arr:
        if j < 0:
            crime += 1
        elif arr[i] == -1 and arr[i+1] == 1:
            crime += 1
        elif j > 0:
            crime -= 1
        else:
            pass
         
print(crime)
