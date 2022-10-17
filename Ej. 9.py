#Algoritmo que pida tres números y los muestre ordenados (de mayor a menor)
vNum=[]
num=int(input("Dime el primer número "))
vNum.append(num)
num=int(input("Dime el segundo número "))
vNum.append(num)
num=int(input("Dime el tercer número "))
vNum.append(num)

vNum.sort(reverse=True)
print(vNum)
 
print("El mayor es", vNum[0])

ultimo=len(vNum)

print("El menor es", vNum[ultimo-1])

print(max(vNum))
print(min(vNum))
