# 基于seek实现tail -f功能
import time
with open('test.txt', 'rb') as f:
    f.seek(0, 2)
    while True:
        line = f.readline()
        if line:
            print(line.decode('utf-8'))
        else:
            time.sleep(0.2)