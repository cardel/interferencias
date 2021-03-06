import xml.etree.ElementTree as ETI


def leerArchivoEntrada(archivo):

	tree = ETI.parse(archivo)
	root = tree.getroot()

	#Variables auxiliares para almacenar arbol XML
	dict = root[1]
	fallDBOctave=0
	numberofChannels=0
	IDband=0
	presentStations=0
	inputStations=0
	formula=0
	m=0
	b=0

	#Variables de salida
	Fc = []
	C = 0
	NE = 0
	NI = 0
	EP = [] 
	EI = []
	ET = []
	FactorCaidaDecada=0


	for child in dict:	
		if child.get('key') == 'fallDBOctave':
			fallDBOctave = child
		elif child.get('key') == 'ChannelsFormule':
			formula = child
		elif child.get('key') == 'numberofChannels':
			numberofChannels=child
		elif child.get('key') == 'IDband':
			IDband=child
		elif child.get('key') == 'presentStations':
			presentStations=child
		elif child.get('key') == 'inputStations':
			inputStations=child
		else:
			print 'Error', child.tag, child.attrib

	#Lectura del archivo

	#Lectura falloctava

	FactorCaidaDecada = float(fallDBOctave[0].text)

	#Lectura numero de canales
	C = int(float(numberofChannels[0].text))

	#Lectura de formula de canales

	for child in formula:
		for entry in child:
			if entry[0].get('key')=='m':
				m=int(float(entry[0][0].text))
			if entry[0].get('key')=='b':
				b=int(float(entry[0][0].text))


	#Creacion canales
	for i in range(0, C):
		Fc.append(m*float(i)+b)

	#ID band
	Banda = IDband[0].text

	#Estaciones presentes

	for list in presentStations:
		for i in list:
			EPi = [1,2,3,4,5,6,7,[],9,10]
			EPi[9] = i[0].get('key') 
			for element in i[0][0]:
				if element[0].get('key')=='power':
					EPi[0] = float(element[0][0].text)
				elif element[0].get('key')=='h':
                                	EPi[1] = float(element[0][0].text)
				elif element[0].get('key')=='x':
					EPi[2] = float(element[0][0].text)
				elif element[0].get('key')=='y':
					EPi[3] = float(element[0][0].text)
				elif element[0].get('key')=='operator':
					EPi[4] = int(float(element[0][0].text))
                        	elif element[0].get('key')=='hre':
                                	EPi[5] = float(element[0][0].text)
                        	elif element[0].get('key')=='w':
                                	EPi[6] = float(element[0][0].text)
                        	elif element[0].get('key')=='channels':
                                	for arr in element[0][0][0]:
						EPi[7].append(int(float(arr.text)))
                      		elif element[0].get('key')=='umbral':
                                	EPi[8] = float(element[0][0].text)

				
			EP.append(EPi)
				
	#Estaciones que ingresan


	for list in inputStations:
        	for i in list:
                	EIi = [1,2,3,4,5,6,7,[],9,10]
                	EIi[9] = i[0].get('key')
			for element in i[0][0]:
                        	if element[0].get('key')=='power':
                                	EIi[0] = float(element[0][0].text)
                        	elif element[0].get('key')=='h':
                                	EIi[1] = float(element[0][0].text)
                        	elif element[0].get('key')=='x':
                                	EIi[2] = float(element[0][0].text)
                        	elif element[0].get('key')=='y':
                                	EIi[3] = float(element[0][0].text)
                        	elif element[0].get('key')=='operator':
                                	EIi[4] = int(float(element[0][0].text))
                        	elif element[0].get('key')=='hre':
                                	EIi[5] = float(element[0][0].text)
                        	elif element[0].get('key')=='w':
                                	EIi[6] = float(element[0][0].text)
                        	elif element[0].get('key')=='channels':
                                	for arr in element[0][0][0]:
                                        	EIi[7].append(int(float(arr.text)))
                       		elif element[0].get('key')=='umbral':
                                	EIi[8] = float(element[0][0].text)


                	EI.append(EIi)


	for i in EP:
		ET.append(i)

	for i in EI:
		ET.append(i)

	NE = len(EP)
	NI = len(EI)
	
	return [C,NE,NI,EI,EP,ET,Fc,FactorCaidaDecada,Banda]
