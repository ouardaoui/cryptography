import base64
from single_byte_xor_cipher import  single_xor_cipher_second
from repeat_key import  xor_reapeat_key
    
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

def combinations_two(chunks) : 
    output = []
    for i in range(len(chunks)) : 
        for j  in range(i+ 1, len(chunks)) :
            k = (chunks[i], chunks[j])
            output.append(k) 
    return output

def key_size(ct,nbr_guess) : 
    def get_score(size) : 
        chunks = (ct[:size],ct[size: size*2] ,ct[size *2 :size *3],ct[size *3 : size *4])
        avr = 0
        for a ,b in combinations_two(chunks) : 
            avr += hamning_distance(a,b)
        avr /= 6
        return avr / size
    score = [(get_score(size), size) for size in range(2 , 41)]
    score.sort()
    return score[:nbr_guess]

def crack_repeat_key(cipher_txt, key_size) :
    chunks = [cipher_txt[i :: key_size] for i in range(key_size)]
    crack = [ single_xor_cipher_second(chunk) for chunk in chunks ]
    combinate_score = sum(guess[0] for guess in crack ) / key_size
    key = bytes(guess[1] for guess in crack)
    return combinate_score, key

if __name__ == "__main__" : 
    with open("6.txt", "r") as f: 
        content = f.read()
        cipher_byte = base64.b64decode(content)
        cipher_byte = b"Vyc fnqkm spdpv nqo hjfxa qmcg 13 eiha umvl."
        keysizes =  key_size(cipher_byte, 5)
        candidates =  [ crack_repeat_key(cipher_byte, key) for _, key in keysizes ]
        candidates.sort()
        best_condidate = candidates[0]
        best_key = best_condidate[1]
        plaintxt = xor_reapeat_key(cipher_byte,best_key)
        print(plaintxt.decode("ascii"))
        # k = crack_repeat_key(cipher_byte, 29)
        # print(k[1])  