from cryptography.fernet import Fernet
from tkinter import filedialog as fd
filename = fd.askopenfilename()
with open('C:\\Users\\Admin\\Desktop\\cybersec\\filekey.key', 'rb') as filekey:
    key = filekey.read()
fernet = Fernet(key)
  
# opening the encrypted file
with open(filename, 'rb') as enc_file:
    encrypted = enc_file.read()
  
# decrypting the file
decrypted = fernet.decrypt(encrypted)
  
# opening the file in write mode and
# writing the decrypted data
with open(filename, 'wb') as dec_file:
    dec_file.write(decrypted)