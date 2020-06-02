n = int(input())
feeling = ""
i = 1
    
while i <= n-1:
    if i % 2 == 0:
       feeling = feeling + "I love that "
    elif i % 2 != 0:
        feeling += "I hate that "
    else:
        pass

    i += 1

if i == n:
    if i % 2 == 0:
       feeling = feeling + "I love it "
    elif i % 2 != 0:
        feeling += "I hate it "
    else:
        pass

print(feeling)
