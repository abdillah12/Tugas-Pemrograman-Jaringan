import socket
from binascii import hexlify

def convert_ip(s):  

    jml = 0  
   
    for i in range(0, len(s)):  
        if(s[i] == '.'):  
            jml = jml+1  
    if(jml != 3):  
        return 0  
 
    set_val= set()  
    for i in range(0, 256):  
        set_val.add(str(i))  
    jml = 0  
    temp = ""  
    for i in range(0, len(s)):  
        if(s[i] != '.'):  
            temp = temp+s[i]  
        else:  
            if(temp in set_val):  
                jml = jml+1  
            temp = ""  
    if(temp in set_val):  
        jml = jml+1  
  
    if(jml == 4):  
        for alamatIP in [ip]:
            packed_ip_addr = socket.inet_aton(alamatIP)
            unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
            return ("IP Address : {} => Packed: {}, Unpacked: {}".format(ip, hexlify(packed_ip_addr), unpacked_ip_addr)) 
    else:  
        return 'IP tidak valid'  

if __name__ == '__main__':
    ip = input('Masukan IP Address: ')  
    print(convert_ip(ip))  