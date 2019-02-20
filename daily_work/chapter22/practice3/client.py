import socket

ip_port = ('127.0.0.1', 8082)

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
data = tcp_client.connect(ip_port)


while True:
    msg = input('>>').strip()
    if not msg:
        continue
    if msg == 'quit':
        break
    tcp_client.send(msg.encode('gbk'))
    print(1)
    msg_res = tcp_client.recv(1024)
    print(2)
    print(msg_res.decode('gbk'))

tcp_client.close()
