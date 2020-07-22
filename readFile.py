#Programa para calcular el ahorro minimo del 10%
# Martes 2 de Junio 2020
# Ing. Arturo Caicedo
# datos almacenados en TablaAhorros
#cada año es una lista tabla2019, tabla2020, de 12 elementos

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#para ver la tabla en el CMD:
#import shelve
#sv= shelve.open("TablaAhorros")

#for k in sv.keys():
#	print (k)

#for v in sv.values():
#	print(v)quit

#for key, value in sv.items():
#	print(key, ' : ', value)

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


import shelve
import datetime
from datetime import date


def convertirMes(numero):
    if(int(numero)==1): return "Enero"
    elif(int(numero)==2): return "Febrero"
    elif(int(numero)==3): return "Marzo"
    elif(int(numero)==4): return "Abril"
    elif(int(numero)==5): return "Mayo"
    elif(int(numero)==6): return "Junio"
    elif(int(numero)==7): return "Julio"
    elif(int(numero)==8): return "Agosto"
    elif(int(numero)==9): return "Septiembre"
    elif(int(numero)==10): return "Octubre"
    elif(int(numero)==11): return "Noviembre"
    elif(int(numero)==12): return "Diciembre"

    

def IngresarAhorro():

    shelveFile = shelve.open("TablaAhorros")
    

    print("ingrese fecha yyyy,m");
    fechas= input()
    fechas= fechas.split(",")
    #fechas[0] es el año, fechas[1] es el mes
    
    print("ingrese monto en USD para "+ convertirMes(fechas[1]) + " "+str(fechas[0]))
    cantidad=input()
    cantidad= cantidad.replace(",",".")
    cantidad=float(cantidad)
    
    print("ingrese valor USD/COP para "+ convertirMes(fechas[1]) + " "+str(fechas[0]))
    dolarUSD = input()
    dolarUSD = dolarUSD.replace(",",".")
    dolarUSD = float(dolarUSD)

    anual = "tabla"+str(fechas[0]);

    tablaTemp= shelveFile[anual]
    
    tablaTemp[int(fechas[1])-1][0]=cantidad #guarda monto del mes
    tablaTemp[int(fechas[1])-1][1]=dolarUSD #guarda valor dolar del mes

    shelveFile[anual] = tablaTemp;
    shelveFile.close()
    
    print("Datos guardados en TablaAhorros")


def CalcularAhorro():
    shelveFile = shelve.open("TablaAhorros")
    dinero_acumulado = 0
    


    for indices in shelveFile: # ya estan los string tabla2019,..., etc.
        listaTemp= shelveFile[indices]

        for contadorMeses in range(12):  # 12 meses
            dinero_acumulado += listaTemp[contadorMeses][0]*listaTemp[contadorMeses][1] # dinero*USD/COP
            

    print("Dinero ganando: $"+f"{dinero_acumulado:,.2f}" )   
    print("Ahorro 10%: $"+f"{dinero_acumulado*0.1:,.2f}" )
    print("Ahorro 20%: $"+f"{dinero_acumulado*0.2:,.2f}" )
    print("Ahorro 30%: $"+f"{dinero_acumulado*0.3:,.2f}" )
    print("Ahorro 40%: $"+f"{dinero_acumulado*0.4:,.2f}" )
    print("Ahorro 50%: $"+f"{dinero_acumulado*0.5:,.2f}" )
    
def AhorroDiario():
    hoy = datetime.datetime.now()
    today =date.today()
    # fecha de inicio de ahorro o trabajo en 5CA 12 abril 2019
    origen = datetime.datetime(2019,4,12)
    dif = hoy - origen
    print ("dias: ", dif.days)
    print ("Ahorrando $5 USD tendrias hoy ", today, " $",5*dif.days," USD")
    





####inicio del programa

intro1 ="____________________________\nDe cada 10 monedas que estás ganando, guarda una y gasta solamente 9 de ellas. \nPronto verás que tan rápido crece tu bolsillo."
intro2 = "Inicio ahorro Abril 2019, 29 años\n____________________________"

print(intro1);
print(intro2);


while(True):
    print("____________________________")
    print("OPCIONES:")
    print("Ver ahorro a la fecha ........ 1")
    print("Ingresa dinero ............... 2")
    print("Ahorro 5 USD ................. 3")
    print("Para terminar ................ 0")
    print("____________________________")

    entrada = input()


    if(entrada.isnumeric()):
        
        if(int(entrada)==1):
            CalcularAhorro()
        elif(int(entrada)==2):
            IngresarAhorro()
        elif(int(entrada)==3):
            AhorroDiario()    
        else:   
            print("Adios...")
            exit()
    else:
        print("Valor no valido...")
        exit()




