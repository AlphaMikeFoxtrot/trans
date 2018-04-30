import string

ind = list(string.ascii_lowercase)

alp = [i for i in range(1, 27)] 

inpt = int("enter string\n\>")

code = ""

for i in inpt:
    if(i != ' '):
        code += str(ind[alp.index(i)])
        code += "/"
    else:
        code += " "
        
print code

input()
