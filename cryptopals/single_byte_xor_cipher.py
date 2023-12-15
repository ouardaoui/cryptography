from fixed_xor import to_byte_hex,fixed_xor

english_letter_frequency = {
 	'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
 	'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
 	'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
 	'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
 	'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
 	'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
 	'y': .01974, 'z': .00074, ' ': .13000
 }

def get_score(plaintxt):
    score = 0
    for char in plaintxt : 
        if  char in english_letter_frequency: 
            score += english_letter_frequency[char.lower()]
    return score
    
def single_xor_cipher(hexa): 
    best_guess = (0,None)
    byte_cipher = bytes.fromhex(hexa)
    plaintxt = ""
    for k in range(256):
        l = [chr(i ^ k) for i in byte_cipher]
        plaintxt = "".join(map(str,l))
        curr_guess = (get_score(plaintxt),plaintxt)
        best_guess = max(best_guess, curr_guess)
    return best_guess[1]
 
hexa = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
txt = single_xor_cipher(hexa)
#print(txt)

byte_hexa = bytes.fromhex(hexa)

def single_xor_cipher_second(ct) : 
    len_ct = len(ct)
    best_candidate = (float('inf'),0,None)
    ct_freqs = {b: ct.count(b) / len_ct for b in range(256)}   
    for key in range(256) : 
        score = 0
        for lettre, freq in english_letter_frequency.items() : 
            score += abs(freq - ct_freqs[ord(lettre) ^ key])
        candidate = (score, key)
        best_candidate = min(best_candidate, candidate)    
    output =  "".join([chr(i ^ best_candidate[1]) for i in ct])
    return (best_candidate[0],best_candidate[1], output) # score, key,output 

if __name__ ==  "__main__" :
    my = single_xor_cipher_second(bytes.fromhex(hexa))
    print(my)


