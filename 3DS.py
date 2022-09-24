# Es necesario crear un venv y activarlo para que la librería crypto funcione correctamente
# python3 -m venv "nombre del ambiente virtual"
# Se accede a la carpeta del ambiente virtual
# Scripts\activate
# pip install pycryptodome
from Crypto.Cipher import DES3

# Se importa la libreria que contiene los nombres de los algoritmos de hash disponibles
from hashlib import md5

if __name__ == '__main__':
    # Se inicializa la variable de operación en 0
    operation = 0

    # Mientras la opción sea diferente de 3, el bucle se repite
    while operation !=3:
        
        # Se imprime en pantalla las opciones disponibles
        print("Elegir una de las siguientes operaciones:\n1- Encrypt \n2- Decrypt\n3- Salir")
        
        # Se almacena el valor ingresado por parte del usuario en la variable de operation
        operation = input("Tu eleccion: ")
        
        # Si no se selecciona ninguna de las opciones se rompe el ciclo
        if operation not in ['1', '2']:
            break
            
        # Se solicita al usuario la dirección del archivo que se va a encriptar o desencriptar
        file_path = input('File path: ')
        
        # Se escribe la llave que tendrá el archivo para ser encriptado o bien escribir la llave del archivo para desencriptarlo
        key = input('TDES key: ')
        
        # Codificar la clave dada a una clave ASCII de 16 bytes con operación md5
        key_hash = md5(key.encode('ascii')).digest()
        
        # Se hace la conversión de hash md5 a una clave 3DES adecuada para Python3
        tdes_key = DES3.adjust_key_parity(key_hash)
        
        # Cifrado con integración de clave Triple DES, MODE_EAX para Confidencialidad y Autenticación
        # y "nonce" para generar un número aleatorio/pseudoaleatorio que se utiliza para el protocolo de autenticación
        cipher = DES3.new(tdes_key, DES3.MODE_EAX, nonce=b'0')
        
        try:
            # Se abre y lee el archivo que proviene de file_path
            with open(file_path, 'rb') as input_file:
                file_bytes = input_file.read()
        except:
            print("\nEl archivo indicado no existe! Intente de nuevo.\n")
            continue
            
        try:
                
            if operation == '1':
                # Si la opción fue 1, se hace el proceso de encriptación
                new_file_bytes = cipher.encrypt(file_bytes)
                encrypt = True
            else:
                # Si la opción fue 2, se hace el proceso de desencriptar
                new_file_bytes = cipher.decrypt(file_bytes)
                encrypt = False
        except:
            if encrypt == True:
                print("\nNo ha sido posible encriptar el archivo porque ya esta encriptado. Intente desencriptarlo.\n")
                continue
            else:
                print("\nNo ha sido posible desencriptar el archivo porque ya esta encriptado. Intente encriptarlo.\n")
                continue
            
        try:
            
            if encrypt == True:
                print("\nEl contenido encriptado es:\n")
                print(new_file_bytes)
                print('\n')
            else:
                print("\nEl contenido desencriptado es:\n")
                print(new_file_bytes)
                print('\n')
        except:
            continue

        # Escribir valores actualizados en el archivo desde la ruta dada
        with open(file_path, 'wb') as output_file:
            output_file.write(new_file_bytes)
            print('Operation Done!')
    
    
