#Algoritmo que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’ y muestre elmensaje ‘ACEPTADA’ si la nota es mayor o igual a cinco, la edad es mayor 
# o igual a dieciocho y el sexo es ‘F’. En caso de que se cumpla lo mismo, pero el sexo sea‘M’, debei mprimir ‘POSIBLE’. Si no se cumplen dichas condiciones se 
# debe mostrar ‘NO ACEPTADA’.

nota=0
edad=0
sexo=""

nota=(int)(input("¿Nota? "))
edad=(int)(input("¿Edad? "))
sexo=(input("¿Sexo? "))

if(nota>=5 and edad>=18 and sexo=="F"):
    print("ACEPTADA")
if(nota>=5 and edad>=18 and sexo=="M"):
    print("POSIBLE")
else:
    print("NO ACEPTADA")

