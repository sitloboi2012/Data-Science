the = ["working","from","home"]
string = ""
index = 0
while index < len(the):
    word = the[index]
    word = word.upper()
    string = string + word[0]
    index += 1

print(string)
