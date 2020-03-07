'''
Simple client
'''
import socket
import os


def main():
    HOST = '127.0.0.1'
    PORT = 5000
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((HOST, PORT))
    except:
        print('Connection to {} port {} not available!!'.format(HOST, PORT))
        client.close()
        exit(-1)

    running = True
    while running:
        filename = input('File to download? ')
        if filename == 'q':
            print('See you soon!!!')
            break
        client.send(filename.encode())
        data = client.recv(1024)
        data = data.decode()
        if data[:4] == 'ERR:':
            print('File not found in the server!!')
            continue

    client.close()


if __name__ == '__main__':
    main()
