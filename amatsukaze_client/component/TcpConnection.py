import socket
from ipaddress import IPv4Address

class TcpConnection():
    __socket: socket.socket

    def __init__(self) -> None:
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, ip: IPv4Address, port: int) -> None:
        self.__socket.connect((ip.exploded, port))
    
    def send(self, messsage: bytes) -> int:
        return self.__socket.send(messsage)

    def recv(self, length: int) -> bytes:
        return self.__socket.recv(length)

    def __del__(self) -> None:
        self.__socket.close()
