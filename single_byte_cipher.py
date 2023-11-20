import sys

english_letter_frequency = {
 	'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
 	'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
 	'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
 	'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
 	'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
 	'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
 	'y': .01974, 'z': .00074, ' ': .13000
 }


arg = sys.argv 

if len(arg) != 2 : 
    exit() 


def alpha_cout (txt) : 
    count = 0
    for i  in txt: 
        if i.isalpha() : 
            count += 1
    return count


def xor(str, key) : 
    output = ""
    for i in str : 
        output += chr(i ^ key)
    return output

def getscore(txt) : 
    score = 0 
    for char in txt : 
        if char in english_letter_frequency : 
            score +=  english_letter_frequency[char]
    return score 


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
    return k,plaintxt

with open(arg[1],'r') as file :
    output = ""
    score = 0 
    while(content := file.readline()):
        key,txt = get_key(bytes.fromhex(content.strip()))
        var = getscore(txt) 
        if(score < var):
            output = txt
            score = var
    print(output.strip())
