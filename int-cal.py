# programa para calcular el interes compuesto
# script para correr tambien en termux, android
# By Ing. Arturo Caicedo, Martes 10  enero 2020
# ----------- definir variables
vInicial = 0  # capital inicial
tiempo = 0  # tiempo de la inversion en años
interes = 0  # interes
aporteAnual = 0  # aportes a capital cada año
# impuesto, se descuenta sobre la cantidad ganada sobre el pediodo.
impuestos = 0
mesOano = 0  # permite identificar si el periodo ingresado es mes o año
# ----- fin definir variables

# -------- definir funciones -----------


def nomenclatura(mesOano):
    if mesOano == "m":
        return "meses"
    else:
        return "años"


def calcular(vInicial, tiempo, interes, aporteAnual, impuestos, mesOano):

    contador = 1  # arranca en año 1
    periodo = 0  # guarda la cantidad de periodos que se calcula interes
    ganancia = 0  # guarda la ganacia anual
    impuestoValor = 0  # guarda la cantidad que se descuenta por impuestos sobre la ganancia
    potencia = 0  # esta entre 1 para año o 1.5 (3/2) para 18 meses
    valorOriginal = vInicial  # valor inicial de TODA la inversion

    if mesOano == "a":
        periodo = tiempo
        potencia = 1
    elif mesOano == "m":
        periodo = tiempo/18  # periodos de 18 meses, año y medio
        potencia = 1.5
    else:
        print("Error, no es 'a' o 'm'")

    while contador <= periodo:

        VFinal = vInicial*(1+interes/100)**potencia

        ganancia = VFinal-vInicial
        impuestoValor = ganancia*impuestos/100
        ganancia = ganancia-impuestoValor
        VFinal = vInicial + ganancia

        print("--------------------")
        print("periodo " + str(contador))
        print("Valor inicial: " + "$" +
              f"{vInicial:,.2f}" + "    Valor final: " + "$" + f"{VFinal:,.2f}")
        print("Impuesto: " + "$" + f"{impuestoValor:,.2f}")
        print("Ganancia antes de impuesto: " + "$" +
              f"{ganancia+impuestoValor:,.2f}" + "    Ganancia despues de impuesto: " + "$" + f"{ganancia:,.2f}")
        # termina calculos para periodo, a continuacion se reasigna valor inicial

        # valorfinal se convierte en valor inicial para la siguiente iteracion

        vInicial = VFinal+aporteAnual
        contador = contador+1

    # ya acabo iteracion
    print("--------------------")
    print("Inversion inicial: " "$" + f"{valorOriginal:,d}")
    print("Valor Final " + "$" + f"{VFinal:,.2f}")
    print("Aportes anuales " + "$" f"{aporteAnual*(periodo-1):,.2f}")
    print("Ganancia " + "$" +
          f"{VFinal-valorOriginal-aporteAnual*(periodo-1):,.2f}")
    print("Invesion sobre un periodo de " +
          str(tiempo) + " " + nomenclatura(mesOano))
    if mesOano == "m":
        print(str(tiempo/12) + " Años")
# ----- fin definir funciones -----


# incia programa

print()
print("Calculadora de Interes Compuesto")
print()

vInicial = int(input("Ingrese el valor inicial a invertir "))
interes = float(input("Ingrese el interes: "))
tiempo = int(input("Ingrese el tiempo: "))
mesOano = input("Meses (m) o Años (a)? ")
aporteAnual = int(input("¿Aportes anuales? "))
impuestos = float(input("Impuesto, Retefuente "))

print()
print("--------------------")
print("Valor inicial es: " + "$" + f"{vInicial:,d}")
print("Interes es: " + str(interes)+"%")
print("Tiempo es: " + str(tiempo) + " " + nomenclatura(mesOano))
print("Aportes anuales: " + "$"+f"{aporteAnual:,d}")
print("Impuestos por periodo " + str(impuestos) + "%")
print("--------------------")


print()
print("Desglose")


calcular(vInicial, tiempo, interes, aporteAnual, impuestos, mesOano)
print()
