import socket
import subprocess

ip_port = ('127.0.0.1', 8082)

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind(ip_port)
tcp_server.listen(5)

while True:
    print('等待连接...')
    conn, client_address = tcp_server.accept()
    print('客户端连接了：', conn, client_address)
    while True:
        try:
            cmd = conn.recv(1024)
            if not cmd:
                break
            print('收到命令', cmd)
            res = subprocess.Popen(cmd.decode('gbk'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout = res.stdout.read()
            stderr = res.stderr.read()

            if stdout+stderr != b'':
                conn.send(stdout + stderr)
                print(len(stdout + stderr))
            else:
                conn.send('None'.encode('gbk'))
        except Exception as e:
            break
    conn.close()
    print('当前连接断开')

tcp_server.close()

