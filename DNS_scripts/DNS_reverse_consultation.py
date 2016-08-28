
import dns.reversename #Modulo en el que contiene clases para realizar consultas reversas a partir de IP

n = dns.reversename.from_address('127.0.0.1')

print(n) #Obtenemos el nombre del dominio apartir de la direccion de IP

print (dns.reversename.to_address(n)) #Obtenemos una direccion de IP apartir de un nombre de dominio