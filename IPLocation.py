# Garlic To Onion / IP Location


from time import sleep
from colorama import Fore
from ipapi import location

from Banner import banner


ly,lr,g,lg,w = Fore.LIGHTYELLOW_EX,Fore.LIGHTRED_EX,Fore.GREEN,Fore.LIGHTGREEN_EX,Fore.WHITE


def ip_location() :
    
    banner()

    sleep (0.05)
    print (ly , "–•[IP LOCATION]•–———————————————————————————————————————————————————————————")

    sleep (0.05)
    print (ly , "\n [~] ENTER A IP:")

    
    sleep (0.05)
    print (w)
    ip = input(" @G.O>>> ")

    if ip == "0" :
        exit()
        
    elif ip == "" :
        print (lr , "\n [!] ERROR")
        exit()

        
    try :
        loc = location(ip)

        print (g , "\n [+] IP:")
        print (lg , "IP: " + loc["ip"])
        print (" Network: " + loc["network"])
        print (" Version: " + loc["version"])

        print (g , "[+] Location:")
        print (lg , "Country: " + loc["country_name"])
        print (" Center: " + loc["country_capital"])
        print (" City: " + loc["city"])
        print (" Region: " + loc["region"])

        print (g , "[+] Country Information:")
        print (lg , "Languages: " + loc["languages"])
        print (" Timezone: " + loc["timezone"])
        print (" Calling Code: " + loc["country_calling_code"])
        print (" Utc Offset: " + loc["utc_offset"])
        print (" Country Tld: " + loc["country_tld"])
        print (" Currency: " + loc["currency"])
        print (" Currency Name: " + loc["currency_name"])
        print (" Region Code: " + loc["region_code"])
        print (" Country Code: " + loc["country_code"])
        print (" Country Code iso3: " + loc["country_code_iso3"])
        print (" Continent Code: " + loc["continent_code"])
        print (" In Eu: " + str(loc["in_eu"]))
        print (" Postal: " + str(loc["postal"]))
        print (" Latitude: " + str(loc["latitude"]))
        print (" Longitude: " + str(loc["longitude"]))

        
    except :
        print (lr , "\n [!] ERROR")
        exit()


    print (ly , "\n Finish")
