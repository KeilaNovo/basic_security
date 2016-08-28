

import dns.name #Modulo gracias a las clases y utilidades podemos realizar consultas de los dominios

n= dns.name.from_text('www.google.com')
n1 = dns.name.from_text('google.com')
print (n.is_subdomain(n1)) #Realizamos la consulta si n1 es del dominio n (True)

#Si lo hacemos a la inversa obtendremos el resultado negativo (False)
#print (n1.is_subdomain(n))

print (n.relativize(n1))#es el nombre relativo "www"

print (n.labels)
print (n1.labels)
