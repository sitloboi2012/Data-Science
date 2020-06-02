n, k = map(int,input().split())

for i in range(k):
    if n%10 != 0:
        n -= k
    elif n%10 == 0:
        n = n/10
    else:
        pass


print(int(n))
