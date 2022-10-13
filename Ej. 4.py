#Crea un programa que pida al usuario dos números y muestre su división si elsegundo no es cero, o un mensaje de aviso en caso contrario.
num1=0
num2=0
num1=(int)(input("Dime el primer número "))
num2=(int)(input("Dime el segundo número "))

if num2!=0:
    print("Su división es", num1/num2)
else:
    print("El denominador es 0")