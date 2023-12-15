import base64

with open("6.txt","r") as f : 
    content = f.read()
    cipher_byte = base64.b64decode(content)
    
def ham(byte) : 
    return bin(byte).count("1")
# def ham(byte) :
#     byte = (byte & 0x55 ) + ((byte >> 1) & 0x55)
#     byte = (byte & 0x33 ) + ((byte >> 2) & 0x33)
#     byte = (byte & 0x0f ) + ((byte >> 4) & 0x0f)
#     return byte 

def hamning_distance(a,b):
    distance = 0
    if(len(a) != len(b)) : 
        exit("length gap")
    output =  [ i ^ j for i,j in zip(a,b) ]
    for b in output : 
        distance += ham(b)
    return distance    
    
if __name__ == "__main__" : 
    a = b"this is a test"
    b = b"wokka wokka!!!"
    print(hamning_distance(a,b))
    