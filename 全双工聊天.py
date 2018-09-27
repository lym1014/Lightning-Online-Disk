from socket import *
from time import ctime

import threading
import sys

HOST = '127.0.0.1'
PORT = 23457
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)



def Send(sock):
    while True:
        try:
            data = input()
            sock.send(data.encode())
            if data == 'Quit':
                break
        except KeyboardInterrupt:
            sock.send('Quit'.encode())
            break


def Recv(sock):
    while True:
        data = sock.recv(BUFSIZ)
        if data.decode() == 'Quit.':
            print('He/She logout')
            continue
        elif data.decode() == 'Quit':
            break
    print('         %s' % data.decode())


if __name__ == '__main__':
    print('Successful connection')
    while True:
        username = input('Your name(press only Enter to quit): ')
        tcpCliSock.send(username.encode())
        if not username:
            tcpCliSock.close()
            break
        # username is not None
        response = tcpCliSock.recv(BUFSIZ)
        if response.decode() == 'Reuse':
            print('The name is reuse, please set a new one')
            continue
        else:
            print('Welcome!')
            break



    recvMessage = threading.Thread(target=Recv, args=(tcpCliSock, ))
    sendMessage = threading.Thread(target=Send, args=(tcpCliSock, ))
    sendMessage.start()
    recvMessage.start()
    sendMessage.join()
    recvMessage.join()

