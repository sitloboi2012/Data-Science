red , blue = map(int,input().split())

different = 0
same = 0

#Cho chạy loop để tìm ra được tổng số đôi khác màu nhau
#Khi một màu = 0 => thoát loop
#same sẽ bằng 1 đôi (2) + 1
#Nếu chỉ còn 1 chiếc thì return 0

#Khi a == 0 or b == 0 thì sẽ thoát loop để lấy số different

while True:
    red -= 1
    blue -= 1
    different += 1
    if red == 0 or blue == 0:
        break
        False
    else:
        pass


if red % 2 == 0:
    same = int(red/2)
elif blue % 2 == 0:
    same = int(blue/2)
else:
    pass


print(different , same) 



