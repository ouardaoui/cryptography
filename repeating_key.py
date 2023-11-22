import sys

arg = sys.argv

if(len(arg) != 2): 
    exit()
    
key = "ICE"
cipher = ""

for i in range(len(arg[1])) : 
    cipher += chr(ord(key[i % 3]) ^ ord(arg[1][i]))
    
print(cipher.encode().hex())
