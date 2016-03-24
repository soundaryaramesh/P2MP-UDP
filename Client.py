from socket import *
import sys
import os
import math
import time


def no_of_digits(a):
	count=0
	while(a!=0):
		a=a/10
		count=count+1
	return count


def get_seq_no(a):
	if(a==0):
		return '0'*10
	count=no_of_digits(a)
	no_of_zeroes=10-count
	val='0'*no_of_zeroes + '%d' %a
	return val

# Buffer size of client should be smaller than the Server's. Otherwise data loss happens
s=socket(AF_INET,SOCK_DGRAM)
no_of_arg=len(sys.argv)
if(no_of_arg!=4):
	print "expected format python %s <number of hosts> <filename> <MSS> "%(sys.argv[0])
elif int(sys.argv[3])<89 or int(sys.argv[3])>2048:
	print sys.agrv[2]," should be greater than 89 bytes and lesser than 2048 bytes"

else:
	host=[]
	addr=[]
	port=[]
	no_of_hosts=int(sys.argv[1])
	for i in range(no_of_hosts):
		host.append(raw_input("Enter hostname %d " %i))
		port.append(raw_input("Enter port of %d th host" %i))
		port[i]=int(port[i])
		addr.append((host[i],port[i]))

	
		
	#addr=(host,port)
	t0=time.time()
	buff_size=int(sys.argv[3])-47-42
	
	file_name=sys.argv[2]
	file_size=os.stat(file_name).st_size
	print file_size
	seq_no=int(math.ceil(float(file_size)/buff_size))
	print "%d" %seq_no
	for i in range(no_of_hosts):
		while(s.sendto("%d" %seq_no,addr[i])):
			break
	a=addr[:]
	while(len(a)!=0):
		d,ad=s.recvfrom(buff_size)
		a.remove(ad)


	seq=0
	curr_seq=get_seq_no(seq)
	f=open(file_name,'rb')
	data=f.read(buff_size)
	#print data
	s.settimeout(0.5)
	
	while(data):
		
		a=addr[:]
		data=curr_seq+data
		ascii_val=map(ord,data)
		group_val=[]
		for i in range(1,len(ascii_val)):
			group_val.append(ascii_val[i-1]*256+ascii_val[i])
		checksum=reduce(lambda x,y:(x+y)%65536,group_val)
		checksum=checksum^65535
		chksum_string='0'*5+'%d' %checksum
		chksum=chksum_string[-5:]
		#print chksum
		data=data+chksum
		host_resp=0
		while(len(a) is not 0):
			#print "curr seq no is ",curr_seq
			for i in range(len(a)):
				while(s.sendto(data,a[i])):
					break
			
			while(host_resp<no_of_hosts):
				#print "waiting for ack.."
				try:
					ack,ad=s.recvfrom(buff_size)
					#print "ack  = ",ack
					#if(int(curr_seq) is int(ack)):
					host_resp=host_resp+1
				       	a.remove(ad)
				except:
					print "timeout, Sequence number = ",curr_seq
					break
			
			#print t


			
		data=f.read(buff_size)
		seq=seq+1
		curr_seq=get_seq_no(seq)
	total_time=time.time()-t0
	print "Total time is %d"%total_time		
	s.close()
	f.close()

