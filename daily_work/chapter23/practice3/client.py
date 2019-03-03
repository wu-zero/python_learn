import socket
import struct
ip_port = ('127.0.0.1', 8080)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ask_for_time_command = 1

while True:
    flg = input('是否校准事件：yes(y),no(others)?\n').strip()
    if flg == 'y':
        client.sendto(struct.pack('i', ask_for_time_command), ip_port)
        data, addr = client.recvfrom(1024)
        print('time: ', data.decode())