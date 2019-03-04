import sys ,os
path = os.path.dirname(__file__)
sys.path.append(path)
from core import user_src

if __name__ == '__main__':
    user_src.run()
