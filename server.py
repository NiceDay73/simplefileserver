'''
Simple file server
'''
import socket
import os


def main():
    HOST = '127.0.0.1'
    PORT = 5000

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))

    server.listen(2)

    data = server.recv(1024)

    server.close()


if __name__ == '__main__':
    main()
