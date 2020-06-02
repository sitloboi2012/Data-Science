n = int(input())

arr = []

dict ={
    "Tetrahedron":4,
    "Cube":6,
    "Octahedron":8,
    "Dodecahedron":12,
    "Icosahedron":20
}


total = 0

for i in range(n):
    arr.append(input())


for i in arr:
    value = dict.get(i)
    total += value

print(total)
