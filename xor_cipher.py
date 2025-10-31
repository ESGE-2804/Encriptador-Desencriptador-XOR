import random
texto = input("Ingresa el texto a encriptar: ")
encriptado = ""
clave = "".join(random.choice('01') for _ in texto) 
for i in range(len(texto)):
    encriptado += chr(ord(texto[i]) ^ int(clave[i]))
print("Texto Encriptado:", encriptado)
desencriptado = ''
for i in range(len(encriptado)):
    desencriptado += chr(ord(encriptado[i]) ^ int(clave[i]))
print("Texto Desencriptado:", desencriptado)