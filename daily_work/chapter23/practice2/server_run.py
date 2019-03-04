import sys ,os
path = os.path.dirname(__file__)
sys.path.append(path)
from core import server_src
from conf.setting import SERVER_IP_PORT
if __name__ == '__main__':
    server_src.run(SERVER_IP_PORT)
