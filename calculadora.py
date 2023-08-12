number1=int(input("Ingresa un numero"))
number2=int(input("Ingresa otro numero"))

eleccion = 0

while eleccion !=5:
    print("""
    Indique la operacion a realizar:
    
    1)Suma
    2)Resta
    3)Multiplicacion
    4)Division
    5)Salir
    """)
    eleccion = int(input())

    if eleccion == 1:
        print(" ")
        print("Resulatdo: ", number1,"+",number2,"=",number1+number2)

    if eleccion == 2:
        print(" ")
        print("Resulatdo: ", number1,"-",number2,"=",number1-number2)
