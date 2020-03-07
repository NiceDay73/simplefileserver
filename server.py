'''
Simple file server
'''
import socket
import os


def main():
    HOST = '127.0.0.1'
    PORT = 5000

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((HOST, PORT))
    except:
        print('Connection error')
        server.close()
        exit(-1)

    while True:
        server.listen(1)
        print('Server is waiting connections at port {}'.format(PORT))
        try:
            conn, addr = server.accept()
        except:
            print('\nClosing server...')
            break
        print('Connection accepted from {}'.format(addr))
        while True:
            try:
                filename = conn.recv(1024)
            except ConnectionResetError:
                break
            filename = filename.decode()
            if filename == 'Bye':
                break
            try:
                filesize = os.path.getsize(filename)
            except (OSError, FileNotFoundError):
                conn.send(b'ERR: File not found!!')
                continue
            conn.send(str(filesize).encode())
            confirm = conn.recv(1024)
            confirm = confirm.decode()
            if confirm == 'y':
                with open(filename, 'r') as fd:
                    data = fd.read()
                    print(data)
                    conn.send(data.encode())
        print('22')
    print('11')
    server.close()


if __name__ == '__main__':
    main()
