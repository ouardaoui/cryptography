#1234 
#0001 #0010 0011 0100
#000100 100011 0100

import base64
import sys 


argumeent = sys.argv
if len(argumeent) != 2 : 
    exit()

hex_string = argumeent[1]

hex_bytes = bytes.fromhex(hex_string)

base64_encoded = base64.b64encode(hex_bytes)

base64_string = base64_encoded.decode('utf-8')

print(base64_string)


