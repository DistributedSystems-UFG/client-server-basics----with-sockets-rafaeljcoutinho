from socket  import *
from constCS import * #-
s = socket(AF_INET, SOCK_STREAM)
s.bind(("172.31.81.153", 5678))  #-
s.listen(1)           #-
(conn, addr) = s.accept()  # returns new socket and addr. client 
while True:                # forever
  data = conn.recv(1024)   # receive data from client
  if not data: break       # stop if client stopped
  print(bytes.decode(data))
  datas = bytes.decode(data)
  if datas[0] == '1':
      conn.send(str.encode(bytes.decode(data)+"*"))
  if datas[0] == '2':
      conn.send(str.encode("*"+bytes.decode(data)+"*"))
  if datas[0] == '3':
      conn.send(str.encode(bytes.decode(data)+"*-*"))
  if datas[0] == '4':
      conn.send(str.encode("*_*"+bytes.decode(data)+"*_*"))

conn.close()               # close the connection
