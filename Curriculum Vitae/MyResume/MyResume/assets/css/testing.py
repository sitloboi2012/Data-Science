def dget_numb(num1,num2,operation):
    result = 0
    if operation == 1:
        result = num1 + num2
    elif operation == 2:
        result = num1 * num2
    else:
        result = num1
    return result

no1 = 2
no2 = 7
answer = dget_numb(no1,no2,2)
print(answer)
