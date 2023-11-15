def ceaser(txt,shift): 
    cipher = ""
    for c in txt : 
        if c.isalpha(): 
            offset = ord('A') if c.isupper() else ord('a')
            cipher += chr((ord(c)  - offset + shift ) % 26 + offset)
        else: 
            cipher += c 
    return cipher 

def vigenere(txt,key): 
    key = key.upper()
    index = 0
    cipher = ""
    for c in txt : 
        if c.isalpha():
            offset = ord('A') if c.isupper() else ord('a')
            shift = ord(key[index]) - ord('A')
            cipher += chr((ord(c)  - offset + shift ) % 26 + offset)
            index = (index + 1) % len(key)
        else: 
            cipher +=  c 
    return cipher 
