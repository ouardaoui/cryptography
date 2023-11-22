from itertools import combinations as com 
from  base64  import b64decode

english_letter_frequency = {
 	'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
 	'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
 	'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
 	'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
 	'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
 	'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
 	'y': .01974, 'z': .00074, ' ': .13000
 }

def getscore(txt) : 
    score = 0 
    for char in txt : 
        if char in english_letter_frequency : 
            score +=  english_letter_frequency[char]
    return score 

def xor(str, key) : 
    output = ""
    for i in str : 
        output += chr(ord(i) ^ key)
    return output

def get_key(cipher):
    score = 0
    k = 0
    plaintxt = ""
    for key in range(256):
        txt = xor(cipher, key)
        s = getscore(txt)
        if score <  s: 
            plaintxt = txt
            score = s
            k = key
    return k,plaintxt,score

def distance(s1,s2) : 
    d =0 
    # if(len(s1) != len(s2)): 
    #     print("Can t calculate distance")
    #     exit()
    for i,j in zip(s1,s2): 
        if(i != j ):
            d += bin(ord(i) ^ ord(j)).count('1')
    return d
        

def guess_key_size(ct : str) -> list[tuple [float,int]]: 
    def getscore(size : int,ct : str) -> float : 
        chunks = (ct[:size], ct[size: 2 * size] , ct[2 * size : 3 * size] , ct[3*size : 4 * size])
        avg = sum(distance(a,b) for a,b in com(chunks,2)) / 6 
        return avg / size
    score = [(getscore(size, ct),size) for size in range(2,41)]
    score.sort()
    return score 

def crack_repeat_key(ciphertext : str ,  keysize : int) : 
    chunks = [ ciphertext[i :: keysize] for i  in range(keysize) ]
    crack_key = [get_key(chunk) for chunk in chunks]
    combinate_score = sum(guess[2] for guess in crack_key) / keysize
    key = (guess[0] for guess in crack_key) 
    
    print(type(crack_key))
    return combinate_score,key

with open('6.txt','r') as f: 
    b64 = f.read()
ciphertetxt = b64decode(b64)
ciphertetxt_string = ciphertetxt.decode('utf-8')
key_size = guess_key_size(ciphertetxt_string)


bunch_key_size = key_size[:5]   
#candidate = [crack_repeat_key(ciphertetxt_string, guess) for _, guess in  bunch_key_size ]
for _, guess in bunch_key_size : 
    c = crack_repeat_key( ciphertetxt_string,guess)
# 0001 0111 input = 23
# b = (b & 01010101) + (b >> 1 ) & 0x55) = 00010101 + 0000 0001 = 00010110
# 01010101 0x55 
#00010010  + 00000100 = 00010110
#00110011 0x33
#00000110 + 00000001 =  00000111
#00001111 0x0f  