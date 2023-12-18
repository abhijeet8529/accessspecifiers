import socket

ser = socket.socket()
print("socket created")

ser.bind(('localhost',9999))       #connection

ser.listen(3) #clients
print("waiting for the connection.....")


while True:
    
   c, addr =  ser.accept()
   name = c.recv(1024).decode()
   
   print("connected with address",addr , name)
   
   c.send(bytes("welcome to the server",'utf-8'))
   
   
   c.close() 