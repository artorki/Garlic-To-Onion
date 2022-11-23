import socket
from time import sleep
from colorama import Fore
from Banner import banner


ly,lr,lg,w = Fore.LIGHTYELLOW_EX,Fore.LIGHTRED_EX,Fore.LIGHTGREEN_EX,Fore.WHITE


def whois():
    banner()

    sleep(0.05)
    print(ly,"–•[WHOIS]•–———————————————————————————————————————————————————————————")

    sleep(0.05)
    print(ly,"\n [!] ENTER A URL:")

    sleep(0.05)
    print(w)
    url = input(" @G.O>>> ")

    if url == "0" :
        exit()
    elif url == "" :
        print(lr,"\n ERROR")
        exit()
 

    if url[-3:] == "org" or url[-3:] == "com" or url[-3:] == "net":
        server = "whois.internic.net"

    else:
        server =  "whois.iana.org"

    try:
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        s.connect((server,43))
        s.send((url+"\r\n").encode())
        output = s.recv(10000)

        print(lg,"\n " + output.decode())

    except:
        print(lr,"\n ERROR")
        exit()

    print(ly,"\n Finish")