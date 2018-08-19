import socket

mi_socket = socket.socket()
mi_socket.connect(('localhost', 47778))

mi_socket.send(bytes("Que tal guachin? desde el client", 'utf-8'))
respuesta = mi_socket.recv(1024)

print(respuesta.decode('utf-8'))
mi_socket.close()
