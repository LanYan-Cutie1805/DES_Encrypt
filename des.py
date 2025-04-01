from Crypto.Cipher import DES
from Crypto.Util.Padding import pad,unpad

key = b'12341234'
plaintext = b'Hello, World!!!'

cipher = DES.new(key, DES.MODE_ECB)
ciphertext = cipher.encrypt(pad(plaintext, DES.block_size))

print(f"Cipher (hex) : {ciphertext.hex()}") #hex 
print(f"Cipher (unicode) : {ciphertext}") #unicode

decrypted = unpad(cipher.decrypt(ciphertext), DES.block_size)
print(f"Decrypted tex: {decrypted}")