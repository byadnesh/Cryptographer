from cryptography.fernet import Fernet
from tkinter import filedialog as fd


files = fd.askopenfilename()
# opening the key
with open('C:\\Users\\Admin\\Desktop\\cybersec\\filekey.key', 'rb') as filekey:
    key = filekey.read()
  
# using the generated key
fernet = Fernet(key)
  
# opening the original file to encrypt
with open(files, 'rb') as file:
    original = file.read()
      
# encrypting the file
encrypted = fernet.encrypt(original)
  
# opening the file in write mode and 
# writing the encrypted data
with open(files, 'wb') as encrypted_file:
    encrypted_file.write(encrypted)