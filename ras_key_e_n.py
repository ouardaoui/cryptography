from Crypto.PublicKey import RSA

key = RSA.import_key(open('../../.ssh/id_rsa.pub','r').read())
print(key.e)
print(key.n)
