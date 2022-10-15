#Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

texto=""
texto=input("Dime una cadena ")

print(texto.isupper())

if (texto.isupper()==False):
    print("No hay letras mayúsculas en este texto o hay al menos una minúscula en este texto")
else:
    print("Todas las letras de este texto son mayúsculas")
