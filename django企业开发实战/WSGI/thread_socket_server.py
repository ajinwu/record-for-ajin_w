import socket
import threading
import time
import errno

EOL1 = b'\n\n'
EOL2 = b"\n\r\n"
body = """
    hello, world 
"""
response_params = [
    "HTTP/1.0 200 ok",
    "Date: Sun, 27 may 2019 10:23:23 GMT",
    "Content-Type: text/html; charset=utf-8",
    "Content-Length: {}\r\n".format(len(body.encode())),
    body
]
response = "\n".join(response_params)

def handle_connection(conn, addr):
    request = conn.recv(1024)
    print(request)
    current_thread = threading.currentThread()
    content_length = len(body.format(thread_name = current_thread.name).encode())
    # print(current_thread.name)
    conn.send(response.format(thread_name = current_thread.name,
        length = content_length
    ).encode())
    conn.close()

def main():
    # socket.AF_INET 用于服务器之间的通信
    # socket.SOCK_STREAM用于基于tcp流式通讯
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 端口复用技术
    serversocket.bind(("127.0.0.1", 8000))
    serversocket.listen(10) # 设置backup_log最大排队数量
    serversocket.setblocking(1)
    print("http://127.0.0.1:8000")
    try:
        i = 0
        while True:
            try:
                conn, address = serversocket.accept()
            except socket.error as e:
                # print(e.args[0], errno.EAGAIN)
                if e.args[0] != errno.EAGAIN:
                    raise
                continue
            i += 1
            print(i)
            t = threading.Thread(target = handle_connection, args = (conn, address),
                name = "thread-%s" %i
            )
            t.start()
    finally:
        serversocket.close()

if __name__ == '__main__':
    main()
    