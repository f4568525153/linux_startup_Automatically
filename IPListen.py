import socket

def listen_broadcast(port=12345):
    # 创建一个UDP套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 设置套接字选项以便在同一地址上重新使用
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 绑定套接字到指定端口
    sock.bind(("", port))

    # 开始监听
    while True:
        data, addr = sock.recvfrom(1024)
        print(f"Received message '{data.decode()}' from {addr}")

if __name__ == "__main__":
    listen_broadcast()

