import socket

c = socket.socket()
print('Socket Created!!')

c.bind(('localhost',9999))
print('Waiting for the clients')
c.listen(3)

while True:
    ipaddr,port = c.accept()
    print('Connected with',ipaddr)
    ipaddr.send("WELCOME TO GOOGLE")
    ipaddr.close()
