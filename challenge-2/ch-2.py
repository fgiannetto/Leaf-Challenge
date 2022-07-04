#Función que recibe una lista de listas y la devuelve identificando si el numero es par o impar


filas = int(input ("Introduzca número de filas: "))
columnas = int(input ("Introduzca número de columnas: "))
print("\n")

matriz = []
#matriz = [[1,2,3], [2,3,4],[4,5,6]]
lista = []
lista_nueva = []

for i in range (filas):
    matriz.append([])
    for j in range(columnas):
        numero = int(input("Fila #{}, Columna#{} -> ".format(i+1, j+1)))
        matriz[i].append(numero)

for m in range(len(matriz)):
    for num in matriz[m]:
        if (num % 2) == 0:  
            #print("True".format(num))
            lista.append('True')  
        else:  
            #print("False".format(num))
            lista.append('False')
    lista_nueva.append(lista)
    lista = []

print (lista_nueva)
