#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def escribirSalida(salidas, archivoSalida, tiempoEjecucion):
	
	NE = salidas[0] 
	NI = salidas[1]
	EP = salidas[2]
	EI = salidas[3]
	
	InterferenciaEIsobreEPporC = salidas[4]
	MaxInterferenciaEIsobreEP = salidas[5]
	InterfiereEIsobreEP = salidas[6]
	
	InterferenciaTodosEIsobreEPporC = salidas[7]
	MaxInterferenciaTodosEIsobreEPep = salidas[8]
	InterfiereTodosEIsobreEPeP = salidas[9]
	
	InterferenciaETsobreEPporC = salidas[10]
	MaxInterferenciaETsobreEP = salidas[11]
	InterfiereETsobreEP = salidas[12]

	InterferenciaTodosEPsobreEIporC = salidas[13]
	MaxInterferenciaTodosEPsobreEI = salidas[14]
	InterfiereTodosEPsobreEI = salidas[15]

	InterferenciaETsobreEIporC = salidas[16]
	MaxInterferenciaETsobreEI = salidas[17]
	InterfiereETsobreEI = salidas[18]

	S1= salidas[19]
	S2= salidas[20]
	S3= salidas[21]
	S4= salidas[22]
	S5= salidas[23]
	Alerta= salidas[24]
	Sol= salidas[25]
	

	ArchivoSalida = archivoSalida
	archivo=open(ArchivoSalida,'a')

	archivo.write('<?xml version="1.0" encoding="UTF-8"?>\n')
	archivo.write('<solution authorXML="Carlos Andrés Delgado Saavedra" >\n')

	#Encabezado
	archivo.write('\t<head>\n')
	archivo.write('\t\t<timeOfSolutionInms>'+str(tiempoEjecucion*1000.0)+'</timeOfSolutionInms>\n')
	archivo.write('\t\t<numberOfPresentStations>'+str(NE)+'</numberOfPresentStations>\n')
	archivo.write('\t\t<numberOfInputStations>'+str(NI)+'</numberOfInputStations>\n')
	archivo.write('\t\t<alert>'+str(Alerta)+'</alert>\n')
	archivo.write('\t\t<valid>'+str(Sol)+'</valid>\n')
	archivo.write('\t\t<status>\n')
	archivo.write('\t\t\t<s1>'+str(S1)+'</s1>\n')
	archivo.write('\t\t\t<s2>'+str(S2)+'</s2>\n')
	archivo.write('\t\t\t<s3>'+str(S3)+'</s3>\n')
	archivo.write('\t\t\t<s4>'+str(S4)+'</s4>\n')
	archivo.write('\t\t\t<s5>'+str(S5)+'</s5>\n')
	archivo.write('\t\t</status>\n')
	archivo.write('\t</head>\n')

	#Reporte
	archivo.write('\t<report>\n')
	archivo.write('\t\t<case key="1">\n')

	aux = 0
	for i in EP:
		archivo.write('\t\t\t<station key="'+str(i[9])+'">\n')
		archivo.write('\t\t\t\t<interferencesPerChannel>\n')
		aux2 = 0
		for j in EI:
			archivo.write('\t\t\t\t\t<interferentStation key="'+str(j[9])+'">\n')
			archivo.write('\t\t\t\t\t\t<channels>\n')
			aux3 = 0	
	
			for k in i[7]:
				archivo.write('\t\t\t\t\t\t\t<channel ID="'+str(k)+'">')
        		        archivo.write(str(InterferenciaEIsobreEPporC[aux][aux2][aux3]))
				archivo.write('</channel>\n')
				aux3+=1
			archivo.write('\t\t\t\t\t\t</channels>\n') 
			archivo.write('\t\t\t\t\t</interferentStation>\n')
			aux2+=1
	 	archivo.write('\t\t\t\t</interferencesPerChannel>\n')
	
		archivo.write('\t\t\t\t<totalInterference>\n')

		aux2 = 0
	        for j in EI:
        	        archivo.write('\t\t\t\t\t<interferentStation key="'+str(j[9])+'">')
               		archivo.write(str(MaxInterferenciaEIsobreEP[aux][aux2]))
	                archivo.write('</interferentStation>\n')
        	        aux2+=1
		archivo.write('\t\t\t\t</totalInterference>\n')
		archivo.write('\t\t\t\t<isInterferent>\n')

		aux2=0
		for j in EI:	
        	        archivo.write('\t\t\t\t\t<interferentStation key="'+str(j[9])+'">')
                	archivo.write(str(InterfiereEIsobreEP[aux][aux2]))
			archivo.write('</interferentStation>\n')
        	        aux2+=1
		archivo.write('\t\t\t\t</isInterferent>\n')
		archivo.write('\t\t\t</station>\n')
		aux+=1

	archivo.write('\t\t</case>\n')
	#Caso 2
	archivo.write('\t\t<case key="2">\n')

	aux = 0
	for i in EP:
		archivo.write('\t\t\t<station key="'+str(i[9])+'">\n')
		archivo.write('\t\t\t\t<interferencesInChannel>\n')
		aux2 = 0
		archivo.write('\t\t\t\t\t<channels>\n')
			
		for k in i[7]:
			archivo.write('\t\t\t\t\t\t\t<channel ID="'+str(k)+'">')
	       	        archivo.write(str(InterferenciaTodosEIsobreEPporC[aux][aux2]))
			archivo.write('</channel>\n')
			aux2+=1

		archivo.write('\t\t\t\t\t</channels>\n')
	 	archivo.write('\t\t\t\t</interferencesInChannel>\n')
	
		archivo.write('\t\t\t\t<totalInterference>')
		archivo.write(str(MaxInterferenciaTodosEIsobreEPep[aux]))
		archivo.write('</totalInterference>\n')

		archivo.write('\t\t\t\t<isInterferent>')
		archivo.write(str(InterfiereTodosEIsobreEPeP[aux]))
		archivo.write('</isInterferent>\n')
	
		archivo.write('\t\t\t</station>\n')


		aux+=1

	archivo.write('\t\t</case>\n')

	#Caso 3
	archivo.write('\t\t<case key="3">\n')

	aux = 0
	for i in EP:
		archivo.write('\t\t\t<station key="'+str(i[9])+'">\n')
		archivo.write('\t\t\t\t<interferencesInChannel>\n')
		aux2 = 0
		archivo.write('\t\t\t\t\t<channels>\n')
			
		for k in i[7]:
			archivo.write('\t\t\t\t\t\t\t<channel ID="'+str(k)+'">')
			archivo.write(str(InterferenciaETsobreEPporC[aux][aux2]))
			archivo.write('</channel>\n')
			aux2+=1

		archivo.write('\t\t\t\t\t</channels>\n')
	 	archivo.write('\t\t\t\t</interferencesInChannel>\n')
	
		archivo.write('\t\t\t\t<totalInterference>')
		archivo.write(str(MaxInterferenciaETsobreEP[aux]))
		archivo.write('</totalInterference>\n')

		archivo.write('\t\t\t\t<isInterferent>')
		archivo.write(str(InterfiereETsobreEP[aux]))
		archivo.write('</isInterferent>\n')
	
		archivo.write('\t\t\t</station>\n')


		aux+=1

	archivo.write('\t\t</case>\n')


	#Caso 4
	archivo.write('\t\t<case key="4">\n')

	aux = 0
	for i in EI:
		archivo.write('\t\t\t<station key="'+str(i[9])+'">\n')
		archivo.write('\t\t\t\t<interferencesInChannel>\n')
		aux2 = 0
		archivo.write('\t\t\t\t\t<channels>\n')
			
		for k in i[7]:
			archivo.write('\t\t\t\t\t\t\t<channel ID="'+str(k)+'">')
	       	        archivo.write(str(InterferenciaTodosEPsobreEIporC[aux][aux2]))
			archivo.write('</channel>\n')
			aux2+=1

		archivo.write('\t\t\t\t\t</channels>\n')
 		archivo.write('\t\t\t\t</interferencesInChannel>\n')
	
		archivo.write('\t\t\t\t<totalInterference>')
		archivo.write(str(MaxInterferenciaTodosEPsobreEI[aux]))
		archivo.write('</totalInterference>\n')

		archivo.write('\t\t\t\t<isInterferent>')
		archivo.write(str(InterfiereTodosEPsobreEI[aux]))
		archivo.write('</isInterferent>\n')
	
		archivo.write('\t\t\t</station>\n')
	archivo.write('\t\t</case>\n')

	#Caso 5
	archivo.write('\t\t<case key="5">\n')

	aux = 0
	for i in EI:
		archivo.write('\t\t\t<station key="'+str(i[9])+'">\n')
		archivo.write('\t\t\t\t<interferencesInChannel>\n')
		aux2 = 0
		archivo.write('\t\t\t\t\t<channels>\n')
			
		for k in i[7]:
			archivo.write('\t\t\t\t\t\t\t<channel ID="'+str(k)+'">')
	       	        archivo.write(str(InterferenciaETsobreEIporC[aux][aux2]))
			archivo.write('</channel>\n')
			aux2+=1

		archivo.write('\t\t\t\t\t</channels>\n')
	 	archivo.write('\t\t\t\t</interferencesInChannel>\n')
	
		archivo.write('\t\t\t\t<totalInterference>')
		archivo.write(str(MaxInterferenciaETsobreEI[aux]))
		archivo.write('</totalInterference>\n')

		archivo.write('\t\t\t\t<isInterferent>')
		archivo.write(str(InterfiereETsobreEI[aux]))
		archivo.write('</isInterferent>\n')
		
		archivo.write('\t\t\t</station>\n')

	archivo.write('\t\t</case>\n')

	archivo.write('\t</report>\n')

	archivo.write('</solution>\n')


	archivo.close();

