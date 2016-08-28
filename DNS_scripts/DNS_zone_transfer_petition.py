import dns.query
import dns.zone # En este modulo tenemos clases que nos permite realizar peticiones XFR para la transferencia de zonas
from signal import signal, SIGPIPE, SIG_DFL 



z = dns.zone.from_xfr(dns.query.xfr('173.194.34.200','github.com'))
names = z.nodes.keys()

for n in names:
    print (z[n].to_text(n))
#Si obtenemos un error, debido a que no se habra podido realizar una transferencia de zona
# dado que se trata de una caracteristica restringida en el servidor que hayamos elegido.
#El error de "Connection timeout",  significa que el puerto 53 en el protocolo TCP se encuentra cerrado
#para la maquina remota. 








#Aclaraciones:
#	Peticiones (A)XFR : este tipo de peticiones a servidores de nombre permite replicar bases de datos DNS entre distintos servidores DNS (primario y 
#						secundario). El secundario se encuentra disponible por si el primero se cae. 
#						Gracias a estas peticiones ambas bases de datos estan sincronizadas. 
#	Protocolo TCP: Protocolo de Transmision de Control, uno de los protocolos mas importantes de Internet. Este protocolo garantiza que los datos seran
#				   entregados en su destino sin errores y en el mismo orden en que se enviaron.
#				   Tambien tiene un mecanismo que permite distinguir distintas aplicaciones dentro de la misma maquina, a traves del puerto.
#				   Da soporte a las aplicaciones de Internet (navegadores,clientes FTP,...) y protocolos de aplicacion(SSH, HTTP, FTP,...)
#	FTP : Protocolo de Transferencia de Archivos, protocolo de red para las transferencia de archivos entre sistemas conectados a una red TCP,
#		  basado en una arquitectura cliente-servidor   