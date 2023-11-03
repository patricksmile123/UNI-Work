plainText = open("encrypted.txt", 'r')
distance = int(input("Please input the distance of the Caesar Cypher "))
code = " "
ordvalue = " "
for ch in plainText:
    len(ch) == 1
    ordvalue = ord(ch)
    cipherValue = ordvalue + distance
    if cipherValue > ord('z'):
        cipherValue = ord('a') + distance - (ord)('z') - ordvalue+1
    code += chr(cipherValue)
print(code)
file = open("encrypted.txt", 'w')
file.write(code)
file.close()
print("hello")