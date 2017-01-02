import socket
s = socket.socket(socket.AF.INET, socket.SOCK_STREAM)
s.connect(('localhost', 4242))
s.send('Hello, world')
data = s.recv(1024)
s.close()
print 'Received', 'data'
