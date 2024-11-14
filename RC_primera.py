"""
Ejercicio 1:
Se debe modularizar correctamente, utilizar parámetros opcionales y cumplir reglas de estilo.
No puede haber código repetido, ni funciones que realicen múltiples tareas. No se puede
utilizar sets, diccionarios, ni tuplas.
Una empresa se dedica al almacenamiento y posterior distribución de camisetas de fútbol en
todo el país. Para ello cuentan con 6 depósitos: Tierra del Fuego, Tucumán, Mendoza, Bs
As, Misiones y Santa Fé.
Los depósitos almacenan camisetas de 5 equipos que son las que más se venden:
Barcelona, Inter Miami, PSG, Manchester City y Real Madrid.
Los puntos 2 y 3 deben utilizar la misma función (calcular_totales). La misma debe poder
sumar por filas o por columnas. Además, deberán utilizar la función estimar_stock que recibe
una lista de totales, una lista de strings con el nombre de cada total y reciba por parámetro
cuál es el límite que debe tomar para informar.
Realizar un menú de opciones:
1. Obtener existencias: para ello deberá generar una función que cargue
secuencialmente, de tal forma que la intersección de cada fila y cada columna
corresponda a la cantidad de camisetas de un equipo en un depósito. Esto es carga
secuencial.
2. Mostrar depósitos que tienen en stock más de 10.000 camisetas.
3. Mostrar equipos que hay en stock más de 5.000 camisetas.
4. Obtener máxima cantidad de camisetas de cada equipo. Mostrar en qué depósito se
encuentra.
5. Cargar ventas: se deberá poder cargar ventas de un determinado producto para un
determinado depósito. Esto es carga distribuida o aleatoria. Al cargarse las ventas
se deben restar los productos vendidos del stock y generar una matriz con la
recaudación que reciba el listado de precios por parámetro, en caso de no recibir un
listado deberá tener un precio de 100 cada producto. Utilizar parámetro opcional.
"""
#6 depósitos: Tierra del Fuego, Tucumán, Mendoza, Bs As, Misiones y Santa Fé.
# almacenan camisetas de 5 equipos (Barcelona, Inter Miami, PSG, Manchester City y Real Madrid)

def C_existencias (filas, columnas) -> int:   
    existencias = []
    for i in range (filas):
        fila = []
        for j in range (columnas):
            cantidad = int(input(f"Ingrese la cantidad de camisetas del equipo {j + 1} en el deposito {i + 1}  "))
        fila.append(cantidad)
        existencias.append(filas)
    return existencias

def Cal_totales (existencias, por_filas = True)  -> int:
    totales = []
    if por_filas:
        for fila in existencias: 
            total = 0 
            for valor in fila:
                total += valor
        totales.append(total)
        return totales
    else:
        for j in range(existencias [0]):
            total = 0
            for fila in existencias:
                total += fila[j]
        totales.append(total)
        return totales


def stock (totales, nombres, limite):
    resultado = []
    for i in range (totales):
        if totales [i] > limite:
            resultado.append(nombres[i])
    return resultado

def Max_Existencias (existencias) -> int:
    maximo = []
    for equipo in range(existencias [0]):
        max_cantidad = -1 
        deposito = -1
        for deposito_index in range(existencias):
            if existencias[deposito_index] [equipo] > max_cantidad:
                max_cantidad = existencias [deposito_index] [equipo]
        maximo.append((equipo + 1, deposito +1, max_cantidad))
    return maximo

def cargar_ventas (existencias, ventas, precios=None) -> int :
    if precios == None:
        precios = [100] * existencias [0]
    recaudacion = []
    for i in range(existencias):
        fila_recaudacion = []
    for j in range(existencias[i]):
        if ventas [i] [j] <= existencias [i] [j]:
            existencias [i] [j] -= ventas [i] [j]
            fila_recaudacion.append(ventas [i] [j] * precios [j])
        else:
            fila_recaudacion.append(0)
    recaudacion.append(fila_recaudacion)
    return recaudacion
