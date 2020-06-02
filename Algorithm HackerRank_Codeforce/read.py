user = int(input())

res = list(map(int,str(user)))
count = 0

list2 = []
list3 = []

for i in reversed(res):
    if count % 2 != 0:
        i = i * 2
        if i > 9:
            i = sum(list(map(int,str(i))))
        else:
            res[i] = i *2
        print(res)
    else:
        pass
    count += 1

    if count == 10:
        if sum(res) % 10 == 0:
            print("Valid")
        else:
            print("Unvalid")


    
    
