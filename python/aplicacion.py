#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import funciones as funciones
import xml.etree.ElementTree as ET
import sys
import readXML
import interferencias
import output
import time

#Variables globales
archivoEntrada=''
archivoSalida=''
inicio = time.time()
#Lectura argumentos

for i in range(0, len(sys.argv)):
	if sys.argv[i] == '--input':
		archivoEntrada = sys.argv[i+1]
	if sys.argv[i] == '--output':
		archivoSalida = sys.argv[i+1]



#Lectura archivo XML
entradas = readXML.leerArchivoEntrada(archivoEntrada)

#Ejecucion modelo
salidas = interferencias.calcularInterferencias(entradas)
fin = time.time()
diferencia =  float(fin - inicio)
#Escritura archivo de salida

output.escribirSalida(salidas, archivoSalida, diferencia)
