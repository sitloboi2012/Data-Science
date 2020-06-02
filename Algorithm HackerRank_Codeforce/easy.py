n = int(input())
arr = list(map(int,input().split()))
easy = 0

for i in arr:
    if i == 0:
        easy += 1
    elif i == 1:
        easy += 0
    else:
        pass

if easy == n:
    print("EASY")
else:
    print("HARD")
    