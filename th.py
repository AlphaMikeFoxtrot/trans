import string

alp = list(string.ascii_lowercase)

ind = [i for i in range(1, 27)] 

inpt = raw_input("enter string\n\>")

code = ""

for i in inpt:
    if(i != ' '):
        code += str(ind[alp.index(i)])
        code += "/"
    else:
        code += " "
        
print code

input()
