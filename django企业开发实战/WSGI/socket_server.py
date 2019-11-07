import socket

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

    # request = b""
    request = conn.recv(1024)
    print(request)
    conn.send(response.encode())
    conn.close()

def main():
    # socket.AF_INET 用于服务器之间的通信
    # socket.SOCK_STREAM用于基于tcp流式通讯
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 端口复用技术
    serversocket.bind(("127.0.0.1", 8000))
    serversocket.listen(5) # 设置backup_log最大排队数量
    print("http://127.0.0.1:8000")
    try:
        while True:
            conn, address = serversocket.accept()
            handle_connection(conn, address)
    finally:
        serversocket.close()

if __name__ == '__main__':
    main()
    