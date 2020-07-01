from datetime import datetime as d
from time import sleep
# hosts file placed in the Windows/drivers/etc/ is used by Microsoft Windows OS.
# This file contains mapping of IP addresses to host names.
# Whenever user accesses any host names in this file, browser redirects to its  IP address mapping
# We will use this file to implement Website Bolcker program using Python 3.

redirect_address= "192.168.1.1"                         
# redirects to this  IP address 

website=["instagram.com", "www.instagram.com", "chess.com", "www.chess.com"]
# list of websites to be blocked

path=r"C:\Windows\System32\drivers\etc\hosts"
# adding r in front of string informs python interpretor to store upcoming string as raw string (does not contain any '\n' '\t' special characters)
# path of host file in Windows OS

# Infinite loop

while(True):
    if ((d.now().hour>=9 and d.now().hour<=12) or (d.now().hour>=15 and d.now().hour<=19)):
        print("FOCUS TIME!")
        with open(path,"r+") as sheet:
            page=sheet.read()
            for url in website:
                if url not in page:
                    line=redirect_address+" "+url+" \n"
                    sheet.write(line)
    else:
        with open(path,"r+") as sheet:
            page=sheet.readlines()
            sheet.seek(0)                       # pointer points at the beginning of the file
            for line in page:
                flag=True
                for url in website:
                    if url in line:
                        flag=False
                        break
                if flag:
                    sheet.write(line)

            sheet.truncate()
            # to delete unnecessary lines 
        print("PLAY TIME!")
    sleep(10)
    # program sleeps every 30 seconds