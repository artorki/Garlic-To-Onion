from colorama import Fore as color
from colorama import Fore
from time import sleep
from os import system
from getpass import getuser
from requests import get
from socket import gethostbyname
import socket
from ipapi import location
import nmap


ly,lr,lg,w,g = Fore.LIGHTYELLOW_EX,Fore.LIGHTRED_EX,Fore.LIGHTGREEN_EX,Fore.WHITE,Fore.GREEN


def banner():

    num = 10
    while num >= 0:

        system("cls")

        try:

            r = get("https://google.com")

            sleep(0.05)
            print(Fore.YELLOW,"""
  --██████████-██████████-██████████-██-------██-██████████--██████████-██████████
 |--██---------██------██-██------██-██-------██-██--------------██-----██------██
 |--██---█████-██████████-████████---██-------██-██--------------██-----██------██
 |--██------██-██------██-██------██-██-------██-██--------------██-----██------██
 |--██████████-██------██-██------██-████████-██-██████████------██-----██████████
 |----------------------------------------------------
 |--██████████-████----██-██-██████████-████----██--██
 |--██------██-██-██---██-██-██------██-██-██---██--██       ARTorki - v2
 |--██------██-██--██--██-██-██------██-██--██--██--██
 |--██------██-██---██-██-██-██------██-██---██-██----       Hello  {}
  --██████████-██----████-██-██████████-██----████--██
  """.format(getuser()))
            break


        except:

            print(Fore.YELLOW,"""
  --██████████-██████████-██████████-██-------██-██████████--██████████-██████████
 |--██---------██------██-██------██-██-------██-██--------------██-----██------██
 |--██---█████-██████████-████████---██-------██-██--------------██-----██------██
 |--██------██-██------██-██------██-██-------██-██--------------██-----██------██
 |--██████████-██------██-██------██-████████-██-██████████------██-----██████████
 |----------------------------------------------------
 |--██████████-████----██-██-██████████-████----██--██
 |--██------██-██-██---██-██-██------██-██-██---██--██       ARTorki - v2
 |--██------██-██--██--██-██-██------██-██--██--██--██       Connection Error
 |--██------██-██---██-██-██-██------██-██---██-██----       Closed: {} s
  --██████████-██----████-██-██████████-██----████--██
  """.format(num))

        num-=1

        if num == -1:
            sleep(1.5)
            exit()
        else:
            sleep(1)

def url_ip():
    banner()

    sleep(0.05)
    print(ly,"–•[URL TO IP]•–———————————————————————————————————————————————————————————")

    sleep(0.05)
    print(ly,"\n [!] ENTER A URL:")

    sleep(0.05)
    print(w)
    url = input(" @G.O>>> ").lower()

    if url == "0" :
        exit()
    elif url == "" :
        print(lr,"\n ERROR")
        exit()


    try:
        ip = gethostbyname(url)
        print(lg,"\n [+] IP:",ip)

    except:
        print(lr,"\n ERROR")
    
    print(ly,"\n Finish")

def cloud_flare():
    banner()

    sleep(0.05)
    print(ly,"–•[Cloud Flare]•–———————————————————————————————————————————————————————————")

    sleep(0.05)
    print(ly,"\n [!] ENTER A URL:")

    sleep(0.05)
    print(w)
    url = input(" @G.O>>> ").lower()

    if url == "0" :
        exit()
    elif url == "" :
        print(lr,"\n ERROR")
        exit()


    sub_list = ["home","admin","administrator","blog","blogs","shop","downloads","webmail","mail","email","mysql","local","localhost","cpanel","ftp","direct","forums","www","www1","www2","www3","www4","www5","api","server","vpn"]

    try:
        sleep(0.05)
        print(g)
        print(" [+] " + gethostbyname(str(url)) + " : " + url , lg)
    except:
        print(lr,"\n Error")
        exit()

    for i in sub_list :

        try:
            host = str(i) + "." + url
            ip = gethostbyname(str(host))
            loc = location(ip)
            print(" [+] " + loc["country_name"] + " : " + ip + " : " + host)
        except:
            pass
    
    print(ly,"\n Finish")

def ip_location():
    banner()

    sleep(0.05)
    print(ly,"–•[IP LOCATION]•–———————————————————————————————————————————————————————————")

    sleep(0.05)
    print(ly,"\n [!] ENTER A IP:")

    sleep(0.05)
    print(w)
    ip = input(" @G.O>>> ")

    if ip == "0" :
        exit()
    elif ip == "" :
        print(lr,"\n ERROR")
        exit()

    try:
        loc = location(ip)

        print(g,"\n [+] IP:")
        print(lg,"IP: " + loc["ip"])
        print(" Network: " + loc["network"])
        print(" Version: " + loc["version"])

        print(g,"[+] Location:")
        print(lg,"Country: " + loc["country_name"])
        print(" Center: " + loc["country_capital"])
        print(" City: " + loc["city"])
        print(" Region: " + loc["region"])

        print(g,"[+] Country Information:")
        print(lg,"Languages: " + loc["languages"])
        print(" Timezone: " + loc["timezone"])
        print(" Calling Code: " + loc["country_calling_code"])
        print(" Utc Offset: " + loc["utc_offset"])
        print(" Country Tld: " + loc["country_tld"])
        print(" Currency: " + loc["currency"])
        print(" Currency Name: " + loc["currency_name"])
        print(" Region Code: " + loc["region_code"])
        print(" Country Code: " + loc["country_code"])
        print(" Country Code iso3: " + loc["country_code_iso3"])
        print(" Continent Code: " + loc["continent_code"])
        print(" In Eu: " + str(loc["in_eu"]))
        print(" Postal: " + str(loc["postal"]))
        print(" Latitude: " + str(loc["latitude"]))
        print(" Longitude: " + str(loc["longitude"]))

    except:
        print(lr,"\n ERROR")
        exit()


    print(ly,"\n Finish")

def port_scanner():
    banner()

    sleep(0.05)
    print(ly,"–•[PORT SCANNER]•–———————————————————————————————————————————————————————————")

    sleep(0.05)
    print(ly,"\n [!] ENTER A IP:")

    sleep(0.05)
    print(w)
    ip = input(" @G.O>>> ")

    if ip == "0" :
        exit()
    elif ip == "" :
        print(lr,"\n ERROR")
        exit()

    sleep(0.05)
    print(ly,"\n [!] ENTER PORT RANGE:")

    sleep(0.05)
    print(w)
    port = input(" @G.O>>> ")

    if port == "0" :
        exit()
    elif port == "" :
        print(lr,"\n ERROR")
        exit()


    try:
        scanner = nmap.PortScanner()
        scanner.scan(ip,port)
        tcp = scanner[ip]["tcp"].keys()

        for i in tcp:
            service = scanner[ip]["tcp"][i]["name"]
            print(lg," [+] Port {} - {} is Open".format(i,service))

    except:
        print(lr,"\n ERROR")
        exit()

    print(ly,"\n Finish")

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


while True:
    banner()

    print(color.LIGHTYELLOW_EX,"–•[HOME]•–———————————————————————————————————————————————————————————")
    sleep(0.05)
    print(color.LIGHTYELLOW_EX,"\n [01] URL To IP")
    sleep(0.05)
    print(color.LIGHTYELLOW_EX,"[02] Cloud Flare")
    sleep(0.05)
    print(color.LIGHTYELLOW_EX,"[03] IP Location")
    sleep(0.05)
    print(color.LIGHTYELLOW_EX,"[04] Port Sccaner")
    sleep(0.05)
    print(color.LIGHTYELLOW_EX,"[05] Whois")
    sleep(0.05)
    print(color.LIGHTYELLOW_EX,"[00] Exit")
    sleep(0.05)
    print(color.WHITE)
    h_input = input(" @G.O>>> ")


    if h_input == "1" :
        url_ip()

    elif h_input == "2" :
        cloud_flare()

    elif h_input == "3" :
        ip_location()

    elif h_input == "4" :
        port_scanner()

    elif h_input == "5" :
        whois()

    elif h_input == "0" :
        exit()

    else:
        print(color.LIGHTRED_EX,"\n ERROR")
        exit()

    input()