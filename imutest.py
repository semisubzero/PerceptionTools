from socket import *

s = socket(type=SOCK_DGRAM)
s.bind(('169.254.120.38',7503))

while True:
    data,addr = s.recvfrom(1024)
    print(data,addr)
    s.sendto(data,addr)