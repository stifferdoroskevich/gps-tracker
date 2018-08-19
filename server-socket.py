'''
    Simple socket server using threads
'''

import socket
import sys
from thread import *

#HOST = '172.16.1.194'   # Symbolic name meaning all available interfaces
HOST = "gps-tracker.herokuapp.com"
PORT = 8888 # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

#Start listening on socket
s.listen(10)
print 'Socket now listening'


def log(msg):
    with open('log.txt', 'a+') as output_file:
        output_file.write('{0}\n'.format(msg))

#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client

    #infinite loop so that function do not terminate and thread do not end.
    while True:

        #Receiving from client
        data = conn.recv(1024)

        if not data:
            break

        print str(data)
        log(data)

        if data.find("##") > -1:
            conn.send("LOAD")

        if len(data) == 15:
            conn.send("ON")

    #came out of loop
    conn.close()

#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))

s.close()