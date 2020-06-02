a,b,c = map(int,input().split())
d,e,f = map(int,input().split())
n = int(input())

total_cup = a + b + c 
total_med = d + e + f 

if n == 1:
    if total_cup != 0 and total_med != 0 or total_cup + total_med > 1:
        print("NO")
    else:
        print("YES")
elif n > 1:
    if total_cup > 5 and total_med > 10:
        print("NO")
    elif total_cup == 5 and total_cup == 10:
        print("YES")
    elif 0 <= total_cup <= 5 and 0 <= total_med <= 10:
        print("YES")
    else:
        pass


    


