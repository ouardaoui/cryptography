from tools import xor_string
#rc4 require two keys KSA & PRGA 

#KSA 
def ksa_gen(s, key) : 
    j = 0
    for i in range(256) :
        j = (j + s[i] + key[i % len(key)]) % 256 
        tmp = s[i]
        s[i]  = s[j] 
        s[j]  = tmp 



#PRGA
def prga_gen(size,s) : 
    i = 0
    j = 0
    key = []
    for k in range(size): 
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        tmp = s[i]
        s[i]  = s[j] 
        s[j]  = tmp 
        key.append(s[ (s[i] + s[j]) % 256 ])
    return key

def to_string(mylist) : 
    string = ''.join(map(chr,mylist))
    return string

def rc4(txt) : 
    s  = list(range(256))
    key = list(range(1,9))
    ksa_gen(s,key)
    size = len(txt)
    k = prga_gen(size,s)
    cypher = xor_string(txt,to_string(k))
    return cypher
