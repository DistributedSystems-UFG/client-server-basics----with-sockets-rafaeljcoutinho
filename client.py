from socket  import *
from constCS import * #-

s = socket(AF_INET, SOCK_STREAM)
s.connect(("172.31.81.153",5678 )) # connect to server (block until accepted)
s.send(str.encode('4 teste'))  # send some data
data = s.recv(1024)     # receive the response
print (bytes.decode(data))            # print the result
s.close()               # close the connection
