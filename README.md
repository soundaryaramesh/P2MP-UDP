# P2MP-UDP
Instructions:
The P2MP-UDP implements data transfer from a single client to multiple servers.
All the servers(Server.py) should run before running the client.
The Format for running server code:
	python Server.py <port no> <filename> <probability>
The variable host should be assigned to the hostname of the server.(It can be found using ifconfig command).
probability is the fraction of total packets which will be lost.
The format for running client code:
	python Client.py <number of hosts> <filename> <MSS>
It will ask for the hostname and port of all the hosts. The hostname should be same as the one specified in Sever.py code and port should match with corresponding port(command line arguement) given while running Server.py code.
MSS(Maximum Segment Size) specifies the size of packet (Bytes) sent at once.
