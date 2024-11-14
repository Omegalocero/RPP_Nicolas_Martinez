from RC_primera import C_existencias, Cal_totales, stock, Max_Existencias, cargar_ventas

def menu():
    print("1: Obtener existencias")
    print("2: Mostrar depósitos que tienen en stock más de 10.000 camisetas")
    print("3: Mostrar equipos que hay en stock más de 5.000 camisetas. ")
    print("4: Obtener máxima cantidad de camisetas de cada equipo. Mostrar en qué depósito seencuentra")
    print("5: Cargar ventas")
    print("6: Salir...")
    return
    #int(input("Seleccione una opcion...  "))

print("1: Obtener existencias")
print("2: Mostrar depósitos que tienen en stock más de 10.000 camisetas")
print("3: Mostrar equipos que hay en stock más de 5.000 camisetas. ")
print("4: Obtener máxima cantidad de camisetas de cada equipo. Mostrar en qué depósito seencuentra")
print("5: Cargar ventas")
print("6: Salir...")


def main ():
    Filas = 6 #Depocitos 
    Columnas = 5 # Equipos
    Depocitos_en = ["Tierra del Fuego", "Tucumán", "Mendoza", "Bs As", "Misiones", "Santa Fé"]
    Nom_Equipos = ["Barcelona", "Inter Miami", "PSG", "Manchester City",  "Real Madrid"]
    Existencias = []
    ventas = []
    precios = [100]

    
    while True:
        opcion = int(input("Seleccione una opcion...  "))
        if opcion == 1:
            Existencias = C_existencias (Filas, Columnas)
        elif opcion == 2:
            totales =  Cal_totales(Existencias , por_filas = True )
            resultado = stock(totales, Depocitos_en, 10000)
            print("Depocitos con mas de 10.000 camicetas en stock ", resultado)
        elif opcion == 3:
            totales = Cal_totales(Existencias, por_filas = False)
            resultado = stock(totales, Nom_Equipos, 5000)
            print("Maxima cantidad de camicetas por equipo y depocito: ", resultado)
        elif opcion == 4:
            maximo = Max_Existencias(Existencias)
            print("máxima cantidad de camisetas por equipo y depocito: ", maximo)
        elif opcion == 5:
            ventas = cargar_ventas(Filas, Columnas)
            recaudacion = cargar_ventas(Existencias, ventas, precios)
            print("Recaudacion por depocito y equipo: ", recaudacion)
            
        elif opcion == 6:
            print("Saliendo....")
            print("....")
            break
        else:
            print("Opcion no valida... intente nuevamente")

