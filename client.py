import socket,sys,time,threading,os
if (len(sys.argv)!=3):
 print "Correct usage: script, IP address, port number"
 exit()
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((sys.argv[1],int(sys.argv[2])))
def receive_m():
 print client_socket.recv(50)
 while 1:
  try:
   msg=client_socket.recv(1024)
   if (msg[:-4:-1]=="txt"):
    media_rt("txt "+time.asctime( time.localtime(time.time()) )+".txt")
   elif(msg[:-6:-1]=="egami"):
    media_ri("image "+time.asctime( time.localtime(time.time()) )+".jpg")
   else:
    continue
  except:
   continue

def send_m():
 while 1:
  try:
   msg=raw_input()
   client_socket.send(msg)
   if (msg=="txt"):
    media_st()
   elif (msg=="image"):
    media_si()
   else:
    continue
  except:
   continue
def media_st():
 print "MEDIA_ST ON"
 filename=raw_input("ENTER THE FILE NAME:")
 f=open(filename,'r')
 size=os.stat(filename).st_size
 print size
 client_socket.send(str(size))
 while 1:
  if(size<=4096):
   time.sleep(0.01)
   client_socket.send(f.read(size))
   break
  else:
   time.sleep(0.2)
   client_socket.send(f.read(4096))
   size=size-4096
def media_rt(filename):
 print "MEDIA_RT ON"
 size=client_socket.recv(123)
 print filename
 size=int(size)
 data=""
 while 1:
  if (size<=4096):
   time.sleep(0.2)
   data=data+client_socket.recv(size)
   f=open(filename,'w')
   f.write(data)
   f.close()
   print "data received"
   print "thanks for connecting"
   break
  else:
   time.sleep(0.2)
   data=data+client_socket.recv(4096)
   size=size-4096
 
def media_si():
 print "MEDIA_S ON"
 filename=raw_input("ENTER THE FILE NAME:")
 f=open(filename,'rb') 
 size=os.stat(filename).st_size
 print size
 client_socket.send(str(size))
 while 1:
  if(size<=4096):
   time.sleep(0.01)
   client_socket.send(f.read(size))
   break
  else:
   time.sleep(0.2)
   client_socket.send(f.read(4096))
   size=size-4096

def media_ri(filename):
 print "MEDIA_RI ON"
 size=client_socket.recv(123)
 print filename
 size=int(size)
 data=""
 while 1:
  if (size<=4096):
   time.sleep(0.2)
   data=data+client_socket.recv(size)
   f=open(filename,'wb')
   f.write(data)
   f.close()
   print "data received"
   print "thanks for connecting"
   break
  else:
   time.sleep(0.2)
   data=data+client_socket.recv(4096)
   size=size-4096

receive=threading.Thread(target=receive_m)
send=threading.Thread(target=send_m)
receive.start()
send.start()


