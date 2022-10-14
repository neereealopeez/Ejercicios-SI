#Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

texto=""
texto= (str)(input("Dime la cadena "))

print(texto.isupper)

if (texto.isupper==False):
    print("Hay una mayúscula en este texto")
