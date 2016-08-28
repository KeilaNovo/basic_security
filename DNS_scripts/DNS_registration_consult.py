#Para servidores DNS 
import dns
import dns.resolver

ansMX = dns.resolver.query('google.com.','A')
ansMX = dns.resolver.query('google.com.','MX')#buscamos registros para servidores de correo
ansNS = dns.resolver.query('google.com.','NS')#buscamos registros para servidores de nombres
ansA = dns.resolver.query('google.com.','A')#buscamos registros para IPv4
ansAAAA = dns.resolver.query('google.com.','AAAA')#buscamos registros para IPv6
ansSOA = dns.resolver.query('google.com.','SOA')#buscamos registros de tipo SOA('Start Of Authority')
ansTXT = dns.resolver.query('google.com.','TXT')#buscamos registros textuales
#En caso de tener problemas con "dns.resolver.query" añadir un punto al final de URL.Ej:"google.es." en vez de "google.es"


for ans in ansMX:
	print (ans)
for ans in ansNS:
	print( ans)
for ans in ansA:
	print(ans)
for ans in ansAAAA:
	print (ans)
for ans in ansSOA:
	print (ans)
for ans in ansTXT:
	print (ans)


#Aclaraciones:
#	Servidor DNS:servicio de dominios con el que se relaciona direcciones IP con nombres de dominios y viceversa.
#				 Base de datos distribuida y jerarquica. Permite consultar diferentes tipos de registros(emails,... )
#				 Puerto que suele utilizar: 53 (UPD)
#				 Se emplea tambien para realizar backups y transferencias de zona.
#				 Viene definidas una serie de consultas que se puede hacer a un servidor. Tipo de consultas: Direccion IPv4, IPv6, servidor de correo,....
#	Protocolo UDP : protocolo minimo de nivel de transporte orientado a mensajes documentadosen en el RFC 768 de la IEFT.
#					Sencilla interfaz de entre la capa de red y la capa de aplicacion.
#	IPv4/IPv6: cuarta y sexta version del protocolo de Internet(IP). La IPv4 emplea direcciones de 32 bits, muchas de ellas usadas para redes locales (LAN)
#																     La IPv6 emplea direcciones de 128 bits	
#	DNSPython: Libreria de python que nos permite realizar operaciones de consulta de registros contra servidores DNS.
#			   Permite acceso a alto y bajo nivel;el primero por medio de consultas a registros DNS y el segundo, permite la manipulacion directa de zonas, mensajes, nombres y registros.	 
#	Registros del tipo SOA: contiene identificadores del servidor de nombres con autoridad sobre la denominacion y su operador y diversos contadores que 
#							que regulan el funcionamiento general del sistema DNS para la denominacion.