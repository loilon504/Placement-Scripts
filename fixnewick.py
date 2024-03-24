with open('addedTree.txt', 'r') as file:
    content = file.read()
# print(content)
newcontent = ""
dem = 0
component = 0

A = ""
B = ""
C = ""
for i in range(1, len(content)):
    if i and content[i] == '(': dem += 1
    if content[i] == ')': dem -= 1
    if dem == 0 and content[i] == ',': component += 1
    if component == 2 and dem == -1: break
    if content[i] != ',' or dem:
        if component == 0: A += content[i]
        if component == 1: B += content[i]
        if component == 2: C += content[i]
print(A)
print(B)
print(C)

newcontent = "((" + A + "," + C + ")," + B + ");"

with open('addedTree.txt', 'w') as file:
    file.write(newcontent)