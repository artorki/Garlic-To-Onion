# artorki


from time import sleep

from Libs import libs
from Banner import banner
from URLToIP import url_ip
from CloudFlare import cloud_flare
from IPLocation import ip_location
from PortScanner import port_scanner
from Whois import whois


white , green , yellow , red = "\033[0;37m" , "\033[92m" , "\033[93m" , "\033[91m"


libs()


while True :

    banner()


    print (yellow , "–•[HOME]•–———————————————————————————————————————————————————————————")
    
    sleep (0.05)
    print ("\n [01] URL To IP")
    sleep (0.05)
    print ("[02] Cloud Flare")
    sleep (0.05)
    print ("[03] IP Location")
    sleep (0.05)
    print ("[04] Port Sccaner")
    sleep (0.05)
    print ("[05] Whois")
    sleep (0.05)
    print ("[00] Exit")
    
    
    sleep (0.05)
    print (white)
    h_input = input (" @G.O>>> ")
    

    if h_input == "1" or h_input == "01" :
        url_ip()

    elif h_input == "2" or h_input == "02" :
        cloud_flare()

    elif h_input == "3" or h_input == "03" :
        ip_location()

    elif h_input == "4" or h_input == "04" :
        port_scanner()

    elif h_input == "5" or h_input == "05" :
        whois()

    elif h_input == "0" :
        exit()

    else :
        print (red , "\n [!] ERROR")
        exit()

       
    input()
