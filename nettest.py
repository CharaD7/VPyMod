import socket
import sys
from termcolor import colored, cprint

plusr = colored('[+]', 'red', attrs=['reverse', 'blink'])
minusg = colored('[-]', 'green', attrs=['reverse', 'blink'])

def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return

def checkVulns(banner):
    if 'FreeFloat FTP Server (Version 1.00)' in banner:
        print(f"{plusr} FreeFloat FTP Serveris vulnerable.")
    elif '3Com 3CDaemon FTP Server Version 2.0' in banner:
        print(f"{plusr} 3CDaemon FTP Server is vulnerable.")
    elif 'Ability Server 2.34' in banner:
        print(f"{plusr} Ability FTP Server is vulnerable.")
    elif 'Sami FTP Server 2.0.2' in banner:
        print(f"{plusr} Sami FTP Server is vulnerable.")
    else:
        print(f"{minusg} FTP Server is not vulnerable.")
    return

def main():
    portList = [21, 22, 25, 80, 110, 443]
    for x in range(1, 255):
        ip = '192.168.95.' + str(x)
        for port in portList:
            banner = retBanner(ip, port)
            if banner:
                print(f"{plusr} {ip} : {banner}")
                checkVulns((banner))

if __name__ == '__main__':
    main()
