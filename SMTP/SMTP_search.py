import socket
import sys 

target = sys.argv[0] #para recibir por linea de comandos el argumento y el comando que queramos utilizar
command = sys.argv[0]
#Aunque nos salga error "IndexError: list index out of range" al compilarlo, al ejecutarlo le facilitamos un string por lo que funcionara si problemas
try:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #realizaremos una conexion al servidor SMTP mediante un socket TCP/IP
	sock.connect((target,25))
	banner = sock.recv(1024)
	print (banner)
	if '220' in banner: # verificamos que en el banner venga el codigo que designemos ('220'). Con el codigo 220 podemos asumir que estamos conectados
		with open ('users.txt', 'r') as f:#abriremos el fichero donde tendremos una lista de nombres de usuarios y verificaremos que esten en el sistema
			for user in f :
				sock.send(command +''+user)#enviaremos el comando que hemos obtenido por linea de comandos junto con el usuario 
				result = sock.recv(1024)#la respuesta que nos devuelve el servidor
				if '252' in str(result) or '250' in str(result):#Si la respuesta nos devuelve los codigos 252 y 250
					print ("Valid user: " + user)#Habremos obtenido un usuario valido
			f.close()
	sock.close()#cerramos el socket 
except socket.timeout:
	print ("Time out for:"+ target)
except socket.error:
	print ("Timeout for: "+ target)


#Modo de ejecucion del script mediante linea de comandos:
# $ python SMPT_search.py "Direccion de IP" vrfy
#Empleamos el comando 'vrfy' de netcat para poder realizar la comprobacion
