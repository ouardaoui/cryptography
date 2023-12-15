import base64

def hex_to_base64(hexa_string) :
    hexa_byte = bytes.fromhex(hexa_string)
    b64_bin = base64.b64encode(hexa_byte)
    return b64_bin.decode() 

if __name__ == "__main__" : 
    b64 = hex_to_base64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
    print(b64)
