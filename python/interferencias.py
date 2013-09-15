# Autor: Carlos Andres Delgado
# Archivo principal del proyecto
import funciones

# Rutinas para leer archivo de entrada


def calcularInterferencias(entradas):
	
	C=entradas[0]
	NE=entradas[1]
	NI=entradas[2]
	EI=entradas[3]
	EP=entradas[4]
	ET=entradas[5]
	Fc=entradas[6]
	FactorCaidaDecada=entradas[7]
	Banda=entradas[8]

	NT = NI + NE
	#Variables de interferencia
	#Caso 1
	InterferenciaEIsobreEPporC=[]
	MaxInterferenciaEIsobreEP=[]
	InterfiereEIsobreEP=[]

	#Caso 2
	InterferenciaTodosEIsobreEPporC=[]
	MaxInterferenciaTodosEIsobreEPep=[]
	InterfiereTodosEIsobreEPeP=[]

	#Caso 3
	InterferenciaETsobreEPporC=[]
	MaxInterferenciaETsobreEP=[]
	InterfiereETsobreEP=[]

	#Caso 4
	InterferenciaTodosEPsobreEIporC = []
	MaxInterferenciaTodosEPsobreEI = []
	InterfiereTodosEPsobreEI = []

	#Caso 5
	InterferenciaETsobreEIporC = []
	MaxInterferenciaETsobreEI = []
	InterfiereETsobreEI = []


	#Salidas

	Sol=-1
	Alerta=-1
	S1=-1
	S2=-1
	S3=-1
	S4=-1

	#----------------------------------------------------------------------------
	#Restricciones
	#----------------------------------------------------------------------------

	#----------------------------------------------------------------------------
	#Caso 1 Interferencia una de cada estacion solicitante a cada estacion presente
	#----------------------------------------------------------------------------

	# Interferencias por canal de cada estacion presente por cada estacion solicitante
	#----------------------------------------------------------------------------

	for i in range(0,NE):
		InterferenciaEIsobreEPporC.append([])
	
		#Obtener canales estacion presente
		CanalesEP=EP[i][7]
		for j in range(0,NI):		
		
			#Obtener canales estacion solicitante
			CanalesEI=EI[j][7]
		
		
			InterferenciaEIsobreEPporC[i].append([])
		
			for k in CanalesEP:
			
				SignalLevelForChannel=0.0
			
				#Frecuencia del canal de la estacion presente
			
				FrecuenciaEPenMhz = Fc[k-1]
			
				#Sumar aportes de cada canal de la estacion solicitante en un canal de la estacion presente
				for x in CanalesEI:
				
					#potencia en dB estacion solicitante
					PotenciaEIenDB = funciones.convertirdBmadB(EI[j][0])
				
					#frecuencia canal de estacion solicitante ---Revisar unidades-----
					FrecuenciaEIenMhz = Fc[x-1]
				
					#Distancia dos estaciones
					distanciakm = funciones.calcularDistancia(EP[i][2], EP[i][3],EI[j][2], EI[j][3])
				
					#htx
					htx=EI[j][1]
					if distanciakm > 0.0:
						SignalLevelForChannel+=funciones.calcularPotenciadBmenW(funciones.calcularPotenciaPercibidaEnF(PotenciaEIenDB, FrecuenciaEPenMhz, FactorCaidaDecada, FrecuenciaEIenMhz, distanciakm, htx))
			
				InterferenciaEIsobreEPporC[i][j].append(funciones.calcularPotenciaWendBm(SignalLevelForChannel))	
			
	# Maxima interferencia por cada estacion presente por cada estacion solicitante
	#----------------------------------------------------------------------------

	for i in range(0,NE):
	
		CanalesEP=EP[i][7]
		MaxInterferenciaEIsobreEP.append([])
	
		for j in range(0,NI):
		
			MaxInterferenciaEIsobreEP[i].append([])
			MaxInterferenciaEIsobreEP[i][j]=0.0

			for k in range(0,len(InterferenciaEIsobreEPporC[i][j])):
				MaxInterferenciaEIsobreEP[i][j] += funciones.calcularPotenciadBmenW(InterferenciaEIsobreEPporC[i][j][k])
		
			MaxInterferenciaEIsobreEP[i][j]=funciones.calcularPotenciaWendBm(MaxInterferenciaEIsobreEP[i][j])
			
						
	# Una estacion es interferida si y solo el maximo nivel de interferencia es superior al permitido por la estacion
	#----------------------------------------------------------------------------

	for i in range(0,NE):
	
		InterfiereEIsobreEP.append([])
	
		for j in range(0,NI):
		
			InterfiereEIsobreEP[i].append([])

			if MaxInterferenciaEIsobreEP[i][j] > EP[i][8]:
				InterfiereEIsobreEP[i][j] = 1.0
			else:
				InterfiereEIsobreEP[i][j] = 0.0
			
			
	#----------------------------------------------------------------------------
	#Caso 2 Interferencia del conjunto de estaciones solicitantes a cada estacion presente
	#----------------------------------------------------------------------------

	#El nivel de interferencia percibido en un canal c0 de una estacion presente epes la suma de aportes de cada una de las estaciones que ingresan.

	for i in range(0,NE):
		CanalesEP=EP[i][7]
		InterferenciaTodosEIsobreEPporC.append([])
	
	
		for j in CanalesEP:
			Interferencia = 0.0	
			FrecuenciaEPenMhz = Fc[j-1]	
		
			for k in range(0,NI):
			
				#Canales estaciones entrantes
				CanalesEI=EI[k][7]
			
				#potencia en dB estacion solicitante
				PotenciaEIenDB = funciones.convertirdBmadB(EI[k][0])

				#Distancia dos estaciones
				distanciakm = funciones.calcularDistancia(EP[i][2], EP[i][3],EI[k][2], EI[k][3])

				#htx
				htx=EI[k][1]
			
				#Se calcula por cada canal de cada estacion del grupo de estaciones solicitante
				if distanciakm > 0.0:		
					for x in CanalesEI:
						#frecuencia canal de estacion solicitante
						FrecuenciaEIenMhz = Fc[x-1]
						Interferencia += funciones.calcularPotenciadBmenW(funciones.calcularPotenciaPercibidaEnF(PotenciaEIenDB, FrecuenciaEPenMhz, FactorCaidaDecada, FrecuenciaEIenMhz, distanciakm, htx))
			
			InterferenciaTodosEIsobreEPporC[i].append(funciones.calcularPotenciaWendBm(Interferencia))		

	#El nivel maximo de interferencia percibido en una estacion presente ep debido al conjunto de estaciones que ingresan, es el maximo valor encontrado de interferencia percibido en los canales c0 de la estacion presente.

	for i in range(0,NE):
		
		CanalesEP=EP[i][7]
		MaxInterferenciaTodosEIsobreEPep.append(0.0)
	
		for j in range(0,len(CanalesEP)):
		
			MaxInterferenciaTodosEIsobreEPep[i]+=funciones.calcularPotenciadBmenW(InterferenciaTodosEIsobreEPporC[i][j])

	
		MaxInterferenciaTodosEIsobreEPep[i]=funciones.calcularPotenciaWendBm(MaxInterferenciaTodosEIsobreEPep[i])


	#El conjunto de estaciones que ingresan interfieren a una estacion presente ep si el maximo nivel de interferencia en dBm encontrado en una estacion ep supera el valor de interferencia permitido.

	for i in range(0,NE):
	
		if MaxInterferenciaTodosEIsobreEPep[i] > EP[i][8]:
			InterfiereTodosEIsobreEPeP.append(1.0)
		else:
			InterfiereTodosEIsobreEPeP.append(0.0)


	#----------------------------------------------------------------------------
	#Caso 3  Interferencia del total de estaciones sobre las estaciones presentes
	#----------------------------------------------------------------------------

	#El nivel de interferencia percibido en una estacion presente ep debido al resto de estaciones es la suma de aportes de cada una de las estaciones.

	for i in range(0,NE):
		CanalesEP=EP[i][7]
		InterferenciaETsobreEPporC.append([])
	
	
		for j in CanalesEP:
			Interferencia = 0.0		
		
			for k in range(0,NT):
			
				#Canales todas estaciones
				CanalesET=ET[k][7]
			
				#potencia en dB estacion solicitante
				PotenciaEIenDB = funciones.convertirdBmadB(ET[k][0])
			
				#htx	
				htx=ET[k][1]
			
				#Distancia dos estaciones
				distanciakm = funciones.calcularDistancia(EP[i][2], EP[i][3],ET[k][2], ET[k][3])
				if distanciakm > 0.0:
					for x in CanalesET:
						#frecuencia canal de estacion solicitante
						FrecuenciaEIenMhz = Fc[x-1]
						Interferencia += funciones.calcularPotenciadBmenW(funciones.calcularPotenciaPercibidaEnF(PotenciaEIenDB, FrecuenciaEPenMhz, FactorCaidaDecada, FrecuenciaEIenMhz, distanciakm, htx))
			
			InterferenciaETsobreEPporC[i].append(funciones.calcularPotenciaWendBm(Interferencia))		
		
	#El maximo nivel de interferencia percibido en una estacion existente ep debido al resto de estaciones es el maximo percibido en cada uno de sus canales c0

	for i in range(0,NE):
	
		CanalesEP=EP[i][7]
		MaxInterferenciaETsobreEP.append(0.0)
	
		for j in range(0,len(CanalesEP)):
		
			MaxInterferenciaETsobreEP[i]+= funciones.calcularPotenciadBmenW(InterferenciaETsobreEPporC[i][j])


		MaxInterferenciaETsobreEP[i]=funciones.calcularPotenciaWendBm(MaxInterferenciaETsobreEP[i])

	#Una estacion existente epse encuentra interferida debido al resto de estaciones si el maximo nivel de interferencia mayor al permitido 

	for i in range(0,NE):
		if MaxInterferenciaETsobreEP[i] > EP[i][8]:
			InterfiereETsobreEP.append(1.0)
		else:
			InterfiereETsobreEP.append(0.0)

	#--------------------------------------------------------------------------------
	# Caso 4 Interferencia estaciones presentes sobre las estaciones solicitantes
	#--------------------------------------------------------------------------------

	#Nivel de interferencia percibido en una canal de una estacion que ingresa debido al conjunto de estaciones presentes
	for i in range(0,NI):
        	CanalesEI=EI[i][7]
        	InterferenciaTodosEPsobreEIporC.append([])

        	for j in CanalesEI:
                	Interferencia = 0.0

                	for k in range(0,NE):

                        	#Canales todas estaciones
                        	CanalesEP=EP[k][7]

                        	#potencia en dB estacion solicitante
                        	PotenciaEIenDB = funciones.convertirdBmadB(EP[k][0])

                        	#htx    
                        	htx=EP[k][1]

                       		#Distancia dos estaciones
                        	distanciakm = funciones.calcularDistancia(EI[i][2], EI[i][3],EP[k][2], EP[k][3])
                        	if distanciakm > 0.0:
                                	for x in CanalesEP:
                                        	#frecuencia canal de estacion solicitante
                                        	FrecuenciaEIenMhz = Fc[x-1]
                                        	Interferencia += funciones.calcularPotenciadBmenW(funciones.calcularPotenciaPercibidaEnF(PotenciaEIenDB, FrecuenciaEPenMhz, FactorCaidaDecada, FrecuenciaEIenMhz, distanciakm, htx))

                	InterferenciaTodosEPsobreEIporC[i].append(funciones.calcularPotenciaWendBm(Interferencia))


	#Maximo nivel de interferencia en una estacion que ingresa debido al conjunto de estaciones presentes

	for i in range(0,NI):

        	CanalesEI=EI[i][7]
        	MaxInterferenciaTodosEPsobreEI.append(0.0)

        	for j in range(0,len(CanalesEI)):

                	MaxInterferenciaTodosEPsobreEI[i]+=funciones.calcularPotenciadBmenW(InterferenciaTodosEPsobreEIporC[i][j])

		MaxInterferenciaTodosEPsobreEI[i]=funciones.calcularPotenciaWendBm(MaxInterferenciaTodosEPsobreEI[i])

	#Interferencia total, si se supera un nivel de interferencia dado

	for i in range(0,NI):

        	if MaxInterferenciaTodosEPsobreEI[i] > EI[i][8]:
                	InterfiereTodosEPsobreEI.append(1.0)
        	else:
                	InterfiereTodosEPsobreEI.append(0.0)

	#--------------------------------------------------------------------------------
	# Caso 5
	#---------------------------------------------------------------------------------

	#Nivel de interferencia percibido por una estacion que ingresa debido al conjunto de estaciones

	for i in range(0,NI):
        	CanalesEI=EI[i][7]
        	InterferenciaETsobreEIporC.append([])

        	for j in CanalesEI:
                	Interferencia = 0.0
	
                	for k in range(0,NT):

                        	#Canales todas estaciones
                        	CanalesET=ET[k][7]

                        	#potencia en dB estacion solicitante
                        	PotenciaEIenDB = funciones.convertirdBmadB(ET[k][0])

                        	#htx    
                        	htx=ET[k][1]

                        	#Distancia dos estaciones
                        	distanciakm = funciones.calcularDistancia(EI[i][2], EI[i][3],ET[k][2], ET[k][3])
                        	if distanciakm > 0.0:
                                	for x in CanalesET:
                                        	#frecuencia canal de estacion solicitante
                                        	FrecuenciaEIenMhz = Fc[x-1]
                                        	Interferencia += funciones.calcularPotenciadBmenW(funciones.calcularPotenciaPercibidaEnF(PotenciaEIenDB, FrecuenciaEPenMhz, FactorCaidaDecada, FrecuenciaEIenMhz, distanciakm, htx))

                	InterferenciaETsobreEIporC[i].append(funciones.calcularPotenciaWendBm(Interferencia))


	#Maximo nivel de interferencia


	for i in range(0,NI):

        	CanalesEI=EI[i][7]
        	MaxInterferenciaETsobreEI.append(0.0)

        	for j in range(0,len(CanalesEI)):

                	MaxInterferenciaETsobreEI[i]+=funciones.calcularPotenciadBmenW(InterferenciaETsobreEIporC[i][j])

		MaxInterferenciaETsobreEI[i]=funciones.calcularPotenciaWendBm(MaxInterferenciaETsobreEI[i])
	#Interfiere si es mayor a cierto nivel de interferencia
	for i in range(0,NI):

        	if MaxInterferenciaETsobreEI[i] > EI[i][8]:
                	InterfiereETsobreEI.append(1.0)
        	else:
                	InterfiereETsobreEI.append(0.0)

	#---------------------------------------------------------------------------------
	#      			          RESTRICCIONES FINALES
	#---------------------------------------------------------------------------------

	#Si existe interferencia en una estacion presente debido a una estacion que ingresa entonces S1 es 1 en caso contrario es 0

	S1 = 0.0
	for i in InterfiereEIsobreEP:
		for j in i:
			S1 += j	


	if S1 > 0.0:
		 S1 = 1.0


	#Si existe interferencia en una estacion presente debido al conjunto de estaciones que ingrsan entonces S2 es 1 en caso contrario es 0


	S2 = 0.0
	for i in InterfiereTodosEIsobreEPeP:
		S2 += i

	if S2 > 0.0:
		S2 = 1.0


	#Si existe interferencia en una estacion presente debido al conjunto de estaciones entonces S3 es 1 en caso contrario es 0
	S3 = 0.0
	for i in InterfiereETsobreEP:
		S3 += i
	if S3 > 0.0:
		S3 = 1.0

	#Si existe interferencia en una estacion que ingresa debido a las estaciones presentes entonces S4 es 1 en caso contrario es 0

	S4 = 0.0
	for i in InterfiereTodosEPsobreEI:
		S4 += i

	if S4 > 0.0:
		S4 = 1.0


	#Si existe interferencia en una estacion que ingresa debido al conjunto de estaciones entonces S5 es 1 en caso contrario 0

	S5 = 0.0

	for i in InterfiereETsobreEI:
		S5 += i

	if S5 > 0.0:
		S5 = 1.0


	#-------------------------------------------------------------------------------------
	# Viabilidad de la solucion
	#-------------------------------------------------------------------------------------

	if S1+S2+S3 > 0.0:
		Sol = 1.0
	else:
		Sol = 0.0

	if S4+S5 > 0.0:
		Alerta  = 1.0
	else:
		Alerta = 0.0

	return [NE, NI, EP, EI, InterferenciaEIsobreEPporC, MaxInterferenciaEIsobreEP, InterfiereEIsobreEP,InterferenciaTodosEIsobreEPporC, MaxInterferenciaTodosEIsobreEPep, InterfiereTodosEIsobreEPeP, InterferenciaETsobreEPporC, MaxInterferenciaETsobreEP, InterfiereETsobreEP, InterferenciaTodosEPsobreEIporC, MaxInterferenciaTodosEPsobreEI, InterfiereTodosEPsobreEI, InterferenciaETsobreEIporC, MaxInterferenciaETsobreEI, InterfiereETsobreEI, S1, S2, S3, S4, S5, Alerta, Sol]
