key1 = "aaaaa"
key2 = "zzzzz"

def xor_string(s1, s2):
    txt = ""
    for char1 , char2 in zip(s1, s2): 
        c = ord(char1) ^ ord(char2)
        txt = txt + chr(c)
    return txt 


txt = xor_string("ayoub", key1)
txt = xor_string(txt,key2)
txt = xor_string(txt, key1)
k = xor_string("ayoub", key2)
