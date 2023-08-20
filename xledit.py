import openpyxl
from openpyxl import load_workbook
from Crypto.Cipher import AES
key = b'candyisagoodboyy'
cipher = AES.new(key, AES.MODE_EAX)
data = "Welcome to copyassignment.com!".encode()
nonce = cipher.nonce
# encrypt the data
ciphertext = cipher.encrypt(data)
da=str(ciphertext,encoding='latin-1')
# print the encrypted data
print("Cipher text:", ciphertext)
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
# d=cipher.decrypt(ciphertext)
# print(d)
wb=load_workbook(filename='testset.xlsx')
s=wb.active
for a in range(2,5):
    # cipher = AES.new(key, AES.MODE_EAX)
    st="B"    
    st=st+str(a)
    # print(st)
    b=s[st]
    b=b.value
    b=str(b)
    c=b.encode('utf-8')
    et=cipher.encrypt(c)
    # et=et.decode(errors='replace')
    print(et)
    s[st]=str(et)
    wb.save(filename='testset.xlsx')
