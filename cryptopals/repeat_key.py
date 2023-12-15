from itertools import islice,cycle 
from fixed_xor import fixed_xor_byte 

def xor_reapeat_key(plaintext, key) :
    new_key = bytes(islice(cycle(key),len(plaintext)))
    cipher_txt = fixed_xor_byte(plaintext,new_key)
    return cipher_txt.encode()
    

if __name__ == "__main__":
    key = b"ICE"
    plaintext = b'''Burning 'em, if you ain't quick and nimble
    I go crazy when I hear a cymbal'''
    cipher = xor_reapeat_key(plaintext,key)
    print(cipher)
    
