from socket import *
import sys
import random


no_of_arg=len(sys.argv)


if(no_of_arg!=4):
        print "expected format python %s <port no> <filename> <probability>" %(sys.argv[0])

host="10.42.0.42"
port=int(sys.argv[1])
randomList=[]

s=socket(AF_INET,SOCK_DGRAM)
prob = float(sys.argv[3]);
addr=(host,port)
s.bind(addr)
buff_size=2048

msg = 'sequence no. recieved!'
data,address=s.recvfrom(buff_size)
s.sendto(msg,address)

file_name=sys.argv[2]
f=open(file_name,'wb')
#print "The total sequences are :  "
print int(data)
total = int(data)


prob = int(prob*total)
for i in range(prob):
	gen_no=random.randint(0,total-1)	
	"""while(gen_no in randomList):
		gen_no=random.randint(0,total-1)		"""
	randomList.append(gen_no)		
#print len(randomList)
randomList.sort()
print randomList


try:
	data,address=s.recvfrom(buff_size)
	
	count =0	
	while(True):
		
		if(count not in randomList):
			#print "Sequence Number", ack			
			ack=data[0:10]
			ack_no=int(ack)
			#print "seq no is %d"%ack_no
			#print "count is %d"%count
			if(ack_no<count):
				while(not s.sendto(ack,address)):
		       			continue
				count = count-1
				print "	ack < count"
			elif(ack_no==count):
				ascii_val=map(ord,data[:-5])
				group_val=[]
				for i in range(1,len(ascii_val)):
					group_val.append(ascii_val[i-1]*256+ascii_val[i])
				
				checksum=reduce(lambda x,y:(x+y)%65536,group_val)
				chk = data[-5:]
				checksum_calculate=(checksum+int(chk))%65535
				#print checksum_calculate
				if(checksum_calculate==0):
		       			while(not s.sendto(ack,address)):
		       				continue
					#print ack, "sent"
		       			f.write(data[10:-5])
				else:
					print "checksum didn't match!"
					count =count-1
			else:
				print "Sequence no didn't match"
				count = count-1
			
		else:
			print "Packet Loss, Sequence number = %d "%count			
			randomList.remove(count)
			count =count-1
		if(count == total-1):
			#print count is total-1
			raise ValueError()
		data,address=s.recvfrom(buff_size)
		
		count = count+1
except:
	f.close()
	print "File obtained"	

s.close()
