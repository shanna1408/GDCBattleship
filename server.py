from lib import ships, board, faction
import socketserver
import socket

HOST = "127.0.0.1"
PORT = 5000

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
    ...


if __name__ == '__main__':
    main()