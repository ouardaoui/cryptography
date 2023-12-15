def to_byte_hex(hexa) : 
    return bytes.fromhex(hexa)

def fixed_xor(hexa_1,hexa_2):
    output = ""
    if(len(hexa_1) != len(hexa_2)) : 
        exit("length of both should be equal !!!")
    for i,j in zip(to_byte_hex(hexa_1),to_byte_hex(hexa_2)): 
        output += chr(i ^ j)
    return output

def fixed_xor_byte(hexa_1,hexa_2):
    output = ""
    if(len(hexa_1) != len(hexa_2)) : 
        exit("length of both should be equal !!!")
    for i,j in zip(hexa_1,hexa_2): 
        output += chr(i ^ j)
    return output
#a = "686974207468652062756c6c277320657965"
#b = "1c0111001f010100061a024b53535009181c" 
#print(fixed_xor(a,b))
