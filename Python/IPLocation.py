# Garlic To Onion / IP Location


from time import sleep
from ipapi import location

from Banner import banner


white , cyan , green , yellow , red = "\033[0;37m" , "\033[96m" , "\033[92m" , "\033[93m" , "\033[91m"


def ip_location() :
    
    while True :


        banner()

        sleep (0.05)
        print (yellow , "–•[IP LOCATION]•–———————————————————————————————————————————————————————————")


        sleep (0.05)
        print (yellow , "\n [~] ENTER A IP:")
    
        sleep (0.05)
        print (white)
        ip = input (" @G.O>>> ")

        if ip == "0" :
            break
        
        elif ip == "" :
            print (red , "\n [!] ERROR")
            exit()

        
        try :

            loc = location (ip)

            print (green , "\n [+] IP:")
            print ("IP: " + loc["ip"])
            print (" Network: " + loc["network"])
            print (" Version: " + loc["version"])

            print (green , "[+] Location:")
            print ("Country: " + loc["country_name"])
            print (" Center: " + loc["country_capital"])
            print (" City: " + loc["city"])
            print (" Region: " + loc["region"])

            print (green , "[+] Country Information:")
            print ("Languages: " + loc["languages"])
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
            print (red , "\n [!] ERROR")
            exit()


        print (yellow , "\n Finish")

        input()
