## from str import maketrans

intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"

tab = str.maketrans(intab, outtab)

string = str(input("enter the string to convert\n/>"))

encoded = string.translate(tab)

print(encoded)

ch = int(input('press 1 to save to file\n/>'))

if(ch == 1):
    with open('encoded.txt', 'w') as f:
        f.write(encoded)
        print('text write successfull!')
else:
    exit
