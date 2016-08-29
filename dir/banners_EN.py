
import sys 
import socket 

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket IPv4 with TCP protocol

for host in range (80, 100):# The number of the machines is going to search (range)
	ports = open ('ports.txt', 'r')
	vulnbanners = open ('vulnbanners.txt', 'r')
	for port in ports:
		try:
				socket.connect((str(sys.argv[1]+"."+str(host)), int(port))) #We open a connection to each port in the range 80,100,for example
				print("Connecting to "+str(sys.argv[1]+"."+str(host))+" in the port: "+str(port)) # and we concatenate the network segment that the user introduce in the command line 
				socket.settimeout(1)# We give it one second of timeout
				banner = socket.recv(1024) # We get the banner that server return to us
				for vulnbanners in vulnbanners.strip(): # we travel through the banner's list
					if banner.strip() is vulnbanners.strip():# If someone match with the banner the server return to us, we assume that we find a coincidence 
						print ("We have a winner" + banner) #A server is running a vulnerable service
						print ("Host:"+ str(sys.argv[1]+'_'+str(host)))
						print ("Port:"+str(port))

		except: 
			#print 'Error connection to :'tr(sys.argv[1]+'.'+str(host))+':'+ int(port)''
			pass
				#If there is an error we pass to the next port, maybe the machine is turn off or the port isn't connected to that service.

	
#Clarification of concepts:
#1. Socket: abstract concept where two programs (located in two different computers)can exchange any type of data flow. 
#			Is also use like the name of an API (Application Programming Interface) for the Network protocols family IP/TCP
#TCP= Transmission Control Protocol
#host : Computers connected to a network, that provide and use services like file transfer,remote connection,etc...of it.
#		Commonly is known like the place where a web resides. It only have a unique IP address and unique domain.  
