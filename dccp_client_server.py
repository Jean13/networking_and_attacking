#!/usr/bin/python

'''
IMPORTANT: DCCP does not work behind NAT.
See: https://www.kernel.org/doc/Documentation/networking/dccp.txt

Originally written for EkoParty 2016 CTF competition - Congested Service (Misc 100)

'''

import socket

socket.DCCP_SOCKOPT_PACKET_SIZE = 1
socket.DCCP_SOCKOPT_SERVICE     = 2
socket.SOCK_DCCP                = 6
socket.IPPROTO_DCCP             = 33
socket.SOL_DCCP                 = 269
packet_size                     = 256

# Server address - modify accordingly
address                         = ('7e0a98bb084ec0937553472e7aafcf68ff96baf4.ctf.site',20000)

try:
	print "[!] WARNING: DCCP does not work behind NAT "
	print "[*] You may ignore this warning if not behind NAT "
	
	# Create sockets
	server,client = [socket.socket(socket.AF_INET, socket.SOCK_DCCP, 
		                       socket.IPPROTO_DCCP) for i in range(2)]
	for s in (server,client):
	    s.setsockopt(socket.SOL_DCCP, socket.DCCP_SOCKOPT_PACKET_SIZE, packet_size)
	    s.setsockopt(socket.SOL_DCCP, socket.DCCP_SOCKOPT_SERVICE, True)

	# Connect sockets - modify accordingly
	server.bind(address)
	server.listen(1)
	client.connect(address)

	print "[*] Connection started... "
	
	client.connect(address)
	s, addr = server.accept()

	print "[*] Received connection from: ", addr

	# Echo
	while 1:
		client.send(input("IN: "))
		print "OUT:", s.recv(1024)
	s.close()

except:
	print "[*] Connection closed.\n"

