
#Bắt đầu từ số lớn nhất để optimise số lượng xu đổi được (dùng reverse và sau đó for loop bình thường)
n = int(input())
denom = [1, 5, 10, 20, 100]
denom.reverse()
c = 0

for x in denom:
    if n >= x:
        num = n // x
        n = n - (num * x)
        c += num

print(c)