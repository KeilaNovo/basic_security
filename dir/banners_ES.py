
import sys 
import socket 

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket IPv4 con protocolo TCP

for host in range (80, 100):# Numero de las maquinas que se van a recorrer
	ports = open ('ports.txt', 'r')
	vulnbanners = open ('vulnbanners.txt', 'r')
	for port in ports:
		try:
				socket.connect((str(sys.argv[1]+"."+str(host)), int(port))) #abrimos una conexion a cada uno de los host (80,100)
				print("Connecting to "+str(sys.argv[1]+"."+str(host))+" in the port: "+str(port)) # y concatenamos el segmento de red que el usuario a introducido por linea de comandos
				socket.settimeout(1)# Le damos un segundo de tiempo
				banner = socket.recv(1024) # recuperamos el banner que nos devuelve el servidor
				for vulnbanners in vulnbanners.strip(): # recorremos el listado de banners
					if banner.strip() is vulnbanners.strip():# Si alguno coincide con el banner que nos a devuelto el servidor, asumimos que hemos encontrado
						print ("We have a winner" + banner) #un servidor que esta ejecutando un servicio  que es vulnerable
						print ("Host:"+ str(sys.argv[1]+'_'+str(host)))
						print ("Port:"+str(port))

		except: 
			#print 'Error connection to :'tr(sys.argv[1]+'.'+str(host))+':'+ int(port)''
			pass#Si se produce algun error pasamos al siguiente puerto, puede ser que la maquina este apagada o que el puerto no este conectado a ese servicio


	
#Aclaracioon de conceptos:
#1. Socket: concepto abstracto en el que dos programas (situados en dos ordenadores distintos) puede intercambiar cualquier flujo de datos. 
#			Tambien usado como el nombre de una API (Interfaz de programacion de aplicaciones)para la familia de protocolos de Internet IP/TCP
#TCP= Transmission Control Protocol
#host : ("anfitrion") Computadoreas conectadas a una red, que proveen y utilizan servicios(transferencia de archivos,conexion remota,etc...) de ella.
#		Comunmente se conoce como el lugar donde reside una web. Tienen una direccion de IP unica y un dominio unico.
