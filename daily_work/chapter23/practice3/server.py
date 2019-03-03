import socket
import time
import struct
ask_for_time_command = 1

ip_port = ('127.0.0.1', 8080)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(ip_port)

while True:
    fmt = "%Y-%m-%d %H:%M:%S"
    data, addr = server.recvfrom(1024)

    command = struct.unpack('i',data)[0]
    if command == ask_for_time_command:
        command_str = 'ask_for_time'
        print("command：", command_str)
        time_now = time.strftime(fmt)
        server.sendto(time_now.encode('utf-8'), addr)