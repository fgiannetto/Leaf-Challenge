#Función que recibe un string de números separados por coma y devuelve la sumatoria de ellos
#Valores de ejemplo = 51,2,43,7,23
#Suman 126

entrada_dato = input('Ingrese números separados por coma: ')
print(entrada_dato)

datos_ingresados = entrada_dato.split (',')
print(datos_ingresados)

sumatoria_datos = [int(string) for string in datos_ingresados]

suma = sum(sumatoria_datos)
print(f"La sumatoria de los números ingresados es: {suma}")