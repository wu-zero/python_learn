import socket
from datahandle import send_data,receive_data



ip_port = ('127.0.0.1', 8082)

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
data = tcp_client.connect(ip_port)

res_cache = b''

while True:
    msg = input('>>').strip()
    if not msg:
        continue
    if msg == 'quit':
        break
    #tcp_client.send(msg.encode('gbk'))
    send_data(msg.encode('gbk'), tcp_client.send)
    #msg_res = tcp_client.recv(512)
    msg_res, res_cache = receive_data(res_cache,tcp_client.recv, 512)
    print(msg_res.decode('gbk'))
tcp_client.close()
