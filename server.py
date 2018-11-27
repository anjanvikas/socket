import socket,sys,time,threading,os
if (len(sys.argv)!=3):
 print "Correct usage: script, IP address, port number"
 exit()
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((sys.argv[1],int(sys.argv[2])))
server_socket.listen(2)
loc=[]
def client_thread(conn,addr):
 conn.send("WELCOME TO CHAT\n\nENTER YOUR USERNAME:")
 name=conn.recv(50)
 while 1:
  try:
   msg=conn.recv(1000)
   print "<{}>{}".format(name,msg)
   for i in loc:
    if i!=conn:
     i.send("<{}>{}".format(name,msg))
   if(msg=="txt" or msg=="image"):
    media(conn,addr,name)
   else:
    continue
  except:
   continue
def media(conn,addr,name):
 size=conn.recv(1024)
 print "size received",size
 for i in loc:
  if i!=conn:
   i.send(size)
 size=int(size)
 data=""
 while 1:
  if (size<=4096):
   data=conn.recv(size)
   time.sleep(0.2)
   for i in loc:
    if i!=conn:
     i.send(data)
   print "completed"
   break
  else:  
   data=conn.recv(4096)
   time.sleep(0.2)
   for i in loc:
    if i!=conn:
     i.send(data)
   size=size-4096
   print size,"\n\n\n\n"
        
while 1:
 conn,addr=server_socket.accept()
 loc.append(conn)
 t=threading.Thread(target=client_thread,args=[conn,addr])
 t.start()
