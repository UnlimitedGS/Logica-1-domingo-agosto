# tipos de datos primitivos:

#edad = 18 # int
#altura = 1.75 # float
#nombre = "Juan" # string es una cadena
#es_mayor = True # boolean
# condicional
# es una expresion que califica el estado de una proposicion y ejecuta una rama del codigo dependiente del estado booleano de esa proposicion.

# clasificar el estado de un pedido segun su codigo
# 1: "recibido"
# 2: "preparado"
# 3: "despachado"
# otro: "desconocido"

#if condicion: "condicion"
#    # #ejecuta el codigo que pongammos aca
#else: 
#    # lo que pasa si es falso


#if condicion matizada:
#    # ejecuta si es verdadero
#elif condicon_2: 
#    # ejecuta si esta condicion es verdadera
#else:
#    # ejecuta si ninguna condicion se cumple

# definir como le fue al alumno segun sus notas

#nota = float(input(" Hey, como le fue en el examen de ese cucho... :"))

#if nota >= 3.5:
#    print("le gane a ese cucho")
#else:
#    print("me tire la nota")


n = float(input("ingrese una nota para dictaminar el rango: "))

if n < 0 or n > 5:
    print("dato invalido")
else:
    if n >= 4.6:
       print("sobresaliente")
    else:
        if n >= 4:
            print("alto")
        elif n >= 3:
            print("basico")
        else:
            print("bajo")