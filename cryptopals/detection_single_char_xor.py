from single_byte_xor_cipher import single_xor_cipher_second  

def get_com(line) : 
    to_byte = bytes.fromhex(line.strip())
    ouput = single_xor_cipher_second(to_byte)
    return ouput

with open("4.txt","r") as f : 
    line = f.readline()
    best_output = (float('inf'), 0, None)
    output = get_com(line)
    best_output = min(best_output,output)
    while(line): 
        line = f.readline()
        if  len(line) == 0 :  
            break;
        output = get_com(line)
        print(output)
        best_output = min(best_output,output)
        
print(best_output)