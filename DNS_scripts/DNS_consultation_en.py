import dns.name #Module that contain the classes and the utilities with which we can make consultations of the domains 

n= dns.name.from_text('www.google.com')
n1 = dns.name.from_text('google.com')
print (n.is_subdomain(n1)) #We check if n1 is n's domain (True)

#If we do it in reverse, we will obtain a negative result (False)
#print (n1.is_subdomain(n))

print (n.relativize(n1))# n1 is the relative name , doesn't have "www"

print (n.labels)
print (n1.labels)
