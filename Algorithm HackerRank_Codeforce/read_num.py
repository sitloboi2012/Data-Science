dictionary = {0:"không",1:"một",2:"hai",3:"ba",4:"bốn",5:"năm",6:"sáu",7:"bảy",8:"tám",9:"chín",10:"mười"}

user = int(input())
list(user)

if user <= 10:
    print(dictionary[user])
elif user > 10 and user < 20:
    print(dictionary[10],dictionary[user])



