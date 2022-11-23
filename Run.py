@artorki


from colorama import Fore as color
from time import sleep

from Banner import banner
from URLToIP import url_ip
from CloudFlare import cloud_flare
from IPLocation import ip_location
from PortScanner import port_scanner
from Whois import whois


while True :

    banner ()

    print (color.LIGHTYELLOW_EX , "–•[HOME]•–———————————————————————————————————————————————————————————")
    sleep (0.05)
    print (color.LIGHTYELLOW_EX , "\n [01] URL To IP")
    sleep (0.05)
    print (color.LIGHTYELLOW_EX , "[02] Cloud Flare")
    sleep (0.05)
    print (color.LIGHTYELLOW_EX , "[03] IP Location")
    sleep (0.05)
    print (color.LIGHTYELLOW_EX , "[04] Port Sccaner")
    sleep (0.05)
    print (color.LIGHTYELLOW_EX , "[05] Whois")
    sleep (0.05)
    print (color.LIGHTYELLOW_EX,"[00] Exit")
    sleep (0.05)
    print (color.WHITE)
    h_input = input (" @G.O>>> ")


    if h_input == "1" or h_input == "01" :
        url_ip ()

    elif h_input == "2" or h_input == "02" :
        cloud_flare ()

    elif h_input == "3" or h_input == "03" :
        ip_location ()

    elif h_input == "4" or h_input == "04" :
        port_scanner ()

    elif h_input == "5" or h_input == "05" :
        whois ()

    elif h_input == "0" :
        exit ()

    else:
        print (color.LIGHTRED_EX , "\n ERROR")
        exit ()

    input ()
