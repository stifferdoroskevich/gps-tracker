import socket

mi_socket = socket.socket()
mi_socket.bind(('localhost', 47778))
mi_socket.listen(5)

while True:
    conexion, addr = mi_socket.accept()
    print ("nueva conexion establecida")
    print (addr)

    peticion = conexion.recv(1024)
    print(peticion.decode('utf-8'))
    conexion.send("hola guacho, desde el server".encode('utf-8'))
    conexion.close()
