#Bear and Big Brother Prob

a , b = map(int,input().split())
year = 0

for i in range(10):
    while a <= b:
        a = a * 3
        b = b * 2
        year += 1
    else:
        break

print(year)