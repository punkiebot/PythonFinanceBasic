#programa para calcular pryeccion de ingressos con un ahorro de 5 usd por dia
# Ing. Arturo Caicedo

# fecha de inicio de ahorro o trabajo en 5CA 12 abril 2019

import datetime
from datetime import date

origenTrabajo5ca = datetime.datetime(2019,4,12)
origen18yo= datetime.datetime(2007,6,27)

today= datetime.datetime.now()


dif5ca =  today - origenTrabajo5ca;
dif18yo = today - origen18yo;





def calcular(tiempodeCalculo, interesAnual):
	# print("llamado funcion, el año es {} y el interes anual es {}%\n".format(tiempodeCalculo,interesAnual))
	







while(True):
	
	print("Programa para calcular pryeccion de ingressos con un ahorro de 5 usd por dia.\n tambien muestra aumento con interees\n ")
	print("x para salir")

	tiempodeCalculo = input("Desde que año desea hacer calculo? 2007 o 2019: ")

	if(tiempodeCalculo== "x"):
		print("Goodbye\n")
		exit()
	
	interesAnual = input( "Ingrese interes anual (con punto): ")
	

	calcular(tiempodeCalculo,interesAnual)








	
