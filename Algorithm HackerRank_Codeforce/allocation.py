test_case = int(input())
a,b = map(int,input().split())
house = list(map(int,input().split()))
total = 0
case = 0
temp_list = []
counter = 0

for i in range(len(house)-1):
    total = house[i] + house[i+1]
    if total <= 100:
        case += 2
        if case > 4:
            case = case//2
        temp_list.append(house[i+1])
    else:
        pass



print(case)





