# Garlic To Onion / Cloud Flare


from ipapi import location
from time import sleep
from socket import gethostbyname
from colorama import Fore

from Banner import banner


ly,lr,lg,g,w = Fore.LIGHTYELLOW_EX,Fore.LIGHTRED_EX,Fore.LIGHTGREEN_EX,Fore.GREEN,Fore.WHITE


def cloud_flare() :
    
    banner()

    sleep (0.05)
    print (ly , "–•[Cloud Flare]•–———————————————————————————————————————————————————————————")

    sleep (0.05)
    print (ly , "\n [~] ENTER A URL:")

    
    sleep (0.05)
    print (w)
    url = input(" @G.O>>> ") . lower()

    if url == "0" :
        exit()
        
    elif url == "" :
        print (lr , "\n [!] ERROR")
        exit()


    sub_list = ["home","admin","administrator","blog","blogs","shop","downloads","webmail","mail","email","mysql","local","localhost","cpanel","ftp","direct","forums","www","www1","www2","www3","www4","www5","api","server","vpn"]

    try :
        sleep (0.05)
        print (g)
        print (" [+] " + gethostbyname(str(url)) + " : " + url , lg)
        
    except :
        print (lr , "\n [!] Error")
        exit()

        
    for i in sub_list :

        try :
            host = str(i) + "." + url
            ip = gethostbyname(str(host))
            loc = location(ip)
            print (" [+] " + loc["country_name"] + " : " + ip + " : " + host)
            
        except:
            pass
    
    
    print (ly , "\n Finish")
