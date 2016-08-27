#Script para saber si hay maquinas activas en un segmento de red. (usando el comando "ping")
#Python 3.5

from subprocess import Popen, PIPE

for ip in range (1,255):#el rango de IP en tipo C : 0-255
	ipAddress = '195.168.1.' + str(ip)#el rango del tercer grupo de numeros puede ser: 0-255
	subprocess = Popen (['/sbin/ping','-c 1',ipAddress],stdout=PIPE, stdin=PIPE, stderr=PIPE) #se crea una estancia Popen para poder ejecutar el comando ping
																							#Los flujos de entrada y salida seran del tipo PIPE
	stdout, stderr = subprocess.communicate(input=None)# Usamos el comando "communicate" para capturar el flujo de salida y el flujo de error
	if b"bytes from" in stdout:
		print ('IP:' + ipAddress) 																	






#Aclaraciones: 
#	Protocolo ICPM: protocolo de mensajes que permite saber si una maquina determinada esta disponible o no (intercambio de mensajes)
#					El comando "ping" utiliza el mensaje ICPM "ECHO_REQUEST"para saber si la maquina esta activa.
#					En caso de estar activa enviara enviara un mensaje ICPM de "ECHO_REPLY", dando a conocer su estado. 
#					20 tipos de mensajes ICMP
#   Traceroute: herramienta que se emplea en el analisis del trafico de un paquete por los diferentes routers por los que pasa 
#	Popen: este constructor permite que los argumentos son preparados para el nuevo programa permitiendo que se puedan comunicar los 	
#		   procesos padres con el, a traves de pipes( "tuberias"). Utilizaremos PIPE para ello.  