import struct

HEAD_SIZE = 4

def send_data(body, send_data_fun):
    body_size = len(body)
    head = struct.pack('i',body_size)
    data_byte = head + body
    send_data_fun(data_byte)
    return True

def receive_data(data_cache, get_data_fun,buffersize):
    data = data_cache
    while len(data) < HEAD_SIZE:
        data += get_data_fun(buffersize)
    
    head_data = data[:HEAD_SIZE]
    body_data = data[HEAD_SIZE:]

    body_size = struct.unpack('i',head_data)[0]
    while len(body_data) < body_size:
        body_data += get_data_fun(buffersize)
    
    body = body_data[:body_size]
    data_cache_next = body_data[body_size:]
    return body, data_cache_next


# =========================测试用=============================
def __send_data_fun(data):
    print(len(data))
    print(data)

def __get_data_from_input(buffersize):
    print(buffersize)
    byte_data = input('>>').encode('gbk')
    print(byte_data)
    return byte_data


if __name__ == '__main__':
    send_data(b'aaaaaaaaaa',__send_data_fun)
    send_data(b'aaaaaaaaaa'*60,__send_data_fun)
    print(receive_data(b'\n\x00\x00\x00',__get_data_from_input))
