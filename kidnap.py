## from str import maketrans

import string

outtab = "abcdefghijklmnopqrstuvwxyz"
intab = [i for i in range(1, 27)]

tab = string.maketrans(intab, outtab)

string = raw_input("enter the string to convert\n/>")

encoded = string.translate(tab)

print(encoded)

ch = int(input('press 1 to save to file\n/>'))

if(ch == 1):
    with open('encoded.txt', 'w') as f:
        f.write(encoded)
        print('text write successfull!')
else:
    exit
