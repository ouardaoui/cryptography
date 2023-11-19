import base64
key = [74,109,112,77,52,110]

m = ""
for i in  range(22): 
    m += chr(100 +i)
input = "flag{"+m+"}"

print(len(input))

def encode(encoded_text) :
    decoded_bytes = base64.b64decode(encoded_text.encode("ascii"))
    ecoded_ascii = [byte for byte in decoded_bytes]
    return ecoded_ascii


length = len(input) - len(key) + 1



#cipher = [ord(key) for key in input]

encoded_text = "LEs2fVVxNDMfNHEtcx80cB8nczQfJhVkDHI/Ew=="
cipher = encode(encoded_text)


#cipher = encode("ZmxhZ3tBQUFBQUFBQUFBQUFBQUFBQUFBQUFBfQ==")


for i in range(length):
    for j in range(len(key)):
        cipher[i + j] = cipher[i + j] ^ key[j]

#print(''.join(chr(k) for k in cipher))

first = ord('f') ^ cipher[0]
second = first ^ ord('l') ^ cipher[1]
third = ord('a') ^ second ^ first ^cipher[2]
fourth = ord('g') ^ third ^second ^ first ^cipher[3]
fifth = ord('{') ^ first ^second ^ third ^ fourth ^cipher[4] 
last = ord('}') ^ cipher[27] 


def fun(k):
    for i in range(length):
        for j in range(len(k)):
            cipher[i + j] = cipher[i + j] ^ k[j]
    print(''.join(chr(key) for key in cipher))
    print("-------------------------------------")



for i in range(128):
    output = [first,second,third, fourth,fifth,last]
    fun(output) 

"""
for i in range(length):
    for j in range(len(key)):
        cipher[i + j] = cipher[i + j] ^ key[j]

print(''.join(chr(key) for key in cipher))


first = ord('f') ^ cipher[0]
second = first ^ ord('l') ^ cipher[1]
third = ord('a') ^ second ^ first ^cipher[2]
fourth = ord('g') ^ third ^second ^ first ^cipher[3]
fifth = ord('{') ^ first ^second ^ third ^ fourth ^cipher[4] 
last = ord('}') ^ cipher[27]

for i in range(128):
    output = [first,second,third, fourth,fifth,last]
    output = ' '.join(str(key) for key in output)
    print(''.join(output))   
""" 
