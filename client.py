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

    while True:
        filename = input('File to download? ')
        if filename == 'q':
            print('See you soon!!!')
            client.send(b'Bye')
            break
        client.send(filename.encode())
        filesize = client.recv(1024)
        filesize = filesize.decode()
        if filesize[:4] == 'ERR:':
            print('File not found in the server!!')
            continue
        msg = input('Filesize is: {} bytes. Download?(y/n)'.format(filesize))
        if msg != 'y':
            break
        client.send(msg.encode())
        fd = open('new_' + filename, 'wb')
        retrievedsize = 0
        while True:
            data = client.recv(1024)
            print(data.decode())
            fd.write(data)
            retrievedsize += len(data)
            print(retrievedsize, filesize)
            if retrievedsize >= int(filesize):
                break
        fd.close()

    client.close()


if __name__ == '__main__':
    main()
