# Es necesario crear un venv y activarlo para que la librería crypto funcione correctamente
# python3 -m venv "nombre del ambiente virtual"
# Se accede a la carpeta del ambiente virtual
# Scripts\activate
# pip install pycryptodome
from Crypto.Cipher import DES3
from hashlib import md5
operation = 0
while operation !=3:
    print("Elegir una de las siguientes operaciones:\n1- Encrypt \n2- Decrypt\n3- Salir")
    operation = input("Tu eleccion: ")
    if operation not in ['1', '2']:
        break
    file_path = input('File path: ')
    key = input('TDES key: ')
    
    key_hash = md5(key.encode('ascii')).digest()
    
    tdes_key = DES3.adjust_key_parity(key_hash)
    cipher = DES3.new(tdes_key, DES3.MODE_EAX, nonce=b'0')
    
    with open(file_path, 'rb') as input_file:
        file_bytes = input_file.read()
        
        if operation == '1':
            new_file_bytes = cipher.encrypt(file_bytes)
        else:
            new_file_bytes = cipher.decrypt(file_bytes)
        
    with open(file_path, 'wb') as output_file:
        output_file.write(new_file_bytes)