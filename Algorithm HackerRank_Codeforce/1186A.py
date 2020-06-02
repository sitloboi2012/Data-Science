#problem 1186A.py codeforce
#Description:
#Vus the Cossack holds a programming competition, in which n people participate. He decided to award them all with pens and notebooks. It is known that Vus has exactly m pens and k notebooks.

#Determine whether the Cossack can reward all participants, giving each of them at least one pen and at least one notebook.
#The first line contains three integers n, m, and k (1≤n,m,k≤100) — the number of participants, the number of pens, and the number of notebooks respectively.

n , m , k = map(int,input().split())

if (n == m or m > n) and (n == k or k > n):
    print("Yes")
elif m < n or k < n:
    print("No")
else:
    pass



