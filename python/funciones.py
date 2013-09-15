#Autor: Carlos Andres Delgado
# Este archivo contiene la funciones matematicas que requiere la aplicacion de interferencias

import math

# Esta funcion calcula las perdidas de una transmision utilizando modelo de Hatta ignorando hre
def calcularPerdidasModeloHatta(FrecuenciaTransmisionMhz, distancia, htx):
	Perdidas = 69.55 + 26.16*math.log(FrecuenciaTransmisionMhz, 10) - 13.82*math.log(htx,10) + (44.9-6.55*math.log(htx,10))*math.log(distancia, 10) - 4.78*math.pow(math.log(FrecuenciaTransmisionMhz,10),2) + 18.33*math.log(FrecuenciaTransmisionMhz,10)-40.94
	return Perdidas
	

#Esta funcion calcula la potencia percibida a una distancia en km dada
def calcularPotenciaPercibida(PotenciaTransmisiondB, FrecuenciaTransmisionMhz, distanciakm, htx):
	return PotenciaTransmisiondB - calcularPerdidasModeloHatta(FrecuenciaTransmisionMhz, distanciakm, htx)
	
#Esta funcion calcula la potencia percibida a una distancia dada a una frecuencia dada con una caida de x dB decada definido por el usuario, retorna datos en dBm
def calcularPotenciaPercibidaEnF(PotenciaTransmisiondB, FrecuenciaInteresMhz, FactorCaidaDecada, FrecuenciaTransmisionMhz, distanciakm, htx):
	PotenciaPercibida = calcularPotenciaPercibida(PotenciaTransmisiondB, FrecuenciaTransmisionMhz, distanciakm, htx)
	octavas = math.fabs(math.log(FrecuenciaInteresMhz/FrecuenciaTransmisionMhz,2))
	PerdidaPorOctavas = FactorCaidaDecada*octavas
	return convertirdBadBm(PotenciaPercibida - PerdidaPorOctavas)	
	
#Convertir dB en dBm
def convertirdBadBm(potenciaEndB):
	return potenciaEndB+30
	
#Convertir dBm a dB
def convertirdBmadB(potenciaEndBm):
	return potenciaEndBm-30
	
#Calcular la distancia entre dos puntos en x
def calcularDistancia(x0,y0,x1,y1):
	return math.pow(math.pow(x1-x0,2.0)+math.pow(y1-y0,2.0),0.5)
	
#Obtener potencia dB en W
def calcularPotenciadBmenW(potenciaEndBm):
	return math.pow(10.0, convertirdBmadB(potenciaEndBm)/10.0)
	
#Obtener dB de potencia en W
def calcularPotenciaWendBm(potenciaEnW):
	return convertirdBadBm(10.0*math.log(potenciaEnW, 10.0))



