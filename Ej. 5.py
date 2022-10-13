#Escribe un programa que pida un nombre de usuario y una contraseña y si se haintroducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un
#error.
nombre=""
contraseña=""

nombre=input("¿Nombre de usuario? ")
contraseña= input("¿Contraseña? ")

if (nombre=="pepe"):
        if contraseña=="asdasd":
            print("Ha entrado al sistema")
        else:
            print("¡ERROR!")
else:
            print("¡ERROR!")