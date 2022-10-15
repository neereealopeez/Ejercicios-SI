#Algoritmo que pida tres números y los muestre ordenados (de mayor a menor)
num1=0
num2=0
num3=0
num1= (int)(input("Dime el primer número "))
num2= (int)(input("Dime el segundo número "))
num3= (int)(input("Dime el tercer número "))

if (num1<num2<num3):
    print("El tercer número es mayor")
if (num1>num2>num3):
    print("El primer número es mayor")
if (num1<num2>num3):
    print("El segundo número es mayor")
