# Garlic To Onion / Libs 
  
  
 from Banner import banner 
  
  
 red = '\033[91m' 
  
          
 try :   
     import ipapi 
      
 except : 
     banner() 
     print (red , '[!] Pleas Install ipapi') 
      
      
 try : 
     import requests 
      
 except : 
     banner() 
     print (red , '[!] Pleas Install requests') 
      
      
 try : 
     import socket 
      
 except : 
     banner() 
     print (red , '[!] Pleas Install socket') 

try : 
     import nmap
      
 except : 
     banner() 
     print (red , '[!] Pleas Install nmap')
  

 print()
