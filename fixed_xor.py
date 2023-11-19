import sys 

arg = sys.argv 

if len(arg) > 3 and len(arg[1]) != len(arg(2)): 
    exit()


output = ""
for i,j in zip(arg[1],arg[2]) : 
    output += str(int(i, 16) ^ int(j, 16)) 

print(output) 

