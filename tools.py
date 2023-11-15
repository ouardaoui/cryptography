def xor_string(s1, s2):
    txt = ""
    for char1 , char2 in zip(s1, s2): 
        c = ord(char1) ^ ord(char2)
        txt = txt + chr(c)
    return txt 
