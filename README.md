# Peer to MultiPoint Communication using User-datagram Protocol  
##Usage
The P2MP-UDP implements data transfer from a single client to multiple servers.
The server should run before any of the clients.
The Format for running the servers: <br />
	`python Server.py <port no> <filename> <probability>` <br />
The variable host should be assigned to the hostname of the server.(It can be found using ifconfig command). <br />
Probability is the fraction of total packets which will be lost. <br />
The format for running the client: <br />
	`python Client.py <number of hosts> <filename> <MSS>` <br />
The host name and ports of all the hosts should be entered.<br /> 
MSS(Maximum Segment Size) specifies the size of packet (Bytes) sent at once.
