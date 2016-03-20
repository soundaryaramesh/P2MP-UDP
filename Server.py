from socket import *
import sys
import random

host="10.42.0.42"
port=19000
no_of_arg=len(sys.argv)
randomList=[]

if(no_of_arg!=3):
        print "expected format python %s <filename> <probability>" %(sys.argv[0])

s=socket(AF_INET,SOCK_DGRAM)
prob = float(sys.argv[2]);
addr=(host,port)
s.bind(addr)
buff_size=2048

msg = 'sequence no. recieved!'
data,address=s.recvfrom(buff_size)
s.sendto(msg,address)

file_name=sys.argv[1]
f=open(file_name,'wb')
print "The total sequences are :  "
print int(data)
total = int(data)


prob = int(prob*total)
for i in range(prob):
	gen_no=random.randint(0,total-1)	
	while(gen_no in randomList):
		gen_no=random.randint(0,total-1)		
	randomList.append(gen_no)		
print len(randomList)
randomList.sort()
print randomList


try:
	data,address=s.recvfrom(buff_size)
	print data[11:]
	count =0	
	while(data):
		ack = data[0:10]
		#print ack
		if(count not in randomList):		
			s.sendto(ack,address)
			#print "Sequence Number", ack			
			if(count==0):			
				f.write(data[11:])
			else:
				f.write(data[10:])
			
		else:
			print "Packet Lost"			
			randomList.remove(count)
			count =count-1
		if(count == total-1):
			print count is total-1
			raise ValueError()
		data,address=s.recvfrom(buff_size)
		
		count = count+1
except:
	f.close()
	print "File obtained"	

s.close()
