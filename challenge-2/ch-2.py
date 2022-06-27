#Función que recibe una lista de listas y la devuelve identificando si el numero es par o impar


matriz = [[1,2,3], [2,3,4],[4,5,6]]

lista = []

for m in range(3):
    for num in matriz[m]:
        if (num % 2) == 0:  
            #print("True".format(num))
            lista.append('True')  
        else:  
            #print("False".format(num))
            lista.append('False')
        
print (lista)