table = list(map(str,input()))
hand = list(map(str,input()))

temp_list = []

#Xóa bỏ những khoảng trống trong arr chừa lại phần tử
for i in hand:
    if i == " ":
        hand.remove(i)
    else:
        pass

#Kiểm tra phần tử giống và truyền vào temp_list
for i in table:
    for j in hand:
        if i == j:
            temp_list.append(i)
        else:
            pass
#Nếu temp_list không trống thì print YES và ngược lại
if len(temp_list) == 0:
    print("NO")
else:
    print("YES")







