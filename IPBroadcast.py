#!/usr/bin/python3

import socket
import time
import netifaces as ni

def get_ip_address(interface_name):
    try:
        ip_address = ni.ifaddresses(interface_name)[ni.AF_INET][0]['addr']
        return ip_address
    except ValueError:
        return None

def send_broadcast(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    while True:
        ip_address = get_ip_address('enp1s0')
        if ip_address and ip_address != '127.0.0.1':
            message = "UP Board IP address: {ip_address}"
            sock.sendto(message.encode('utf-8'), ('255.255.255.255', port))
        time.sleep(3)

def main():
    broadcast_port = 50000
    send_broadcast(broadcast_port)

if __name__ == "__main__":
    print("YEEEEEEEE")
    main()

