import socket
from binascii import hexlify

def convert_ip():
    ip = input('Masukan alamat IP : ')
    if ip == '0.0.0.0':
        print('IP Address tidak valid')
    else:
        for ip_addr in [ip]:
            packed_ip_addr = socket.inet_aton(ip_addr)
            unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)

            print("IP Address : {} => Packed: {}, Unpacked: {}".format(ip_addr, hexlify(packed_ip_addr), unpacked_ip_addr))

if __name__ == '__main__':
    convert_ip()