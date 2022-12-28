def main():
    from ssl import SSLCertVerificationError
    import requests
    from subprocess import call
    print("\033[1;31mWarning: ", "\033[0mYour target url should be like http://example.com/search?q=")
    url = input("Enter your target url: ")
    print("\n  Start Scanning be wait...")

    vulnerable = []
    ask_location = input("Enter Location of Xss Payloads text file ( Press Enter to use default ) : ").strip()
    if ask_location == "":
        file = open("Dics\\PayloadsTextFiles\\XssPayloads.txt", "r")  # Open files containing possible admin directories
    else:
        file = open(ask_location, "r")  

    for payload in file.read().splitlines():
        link = url + payload
        r = requests.get(link)
        if payload.lower() in r.text.lower():
            print("\033[1;31m [-] This site is vulnerable to: \033[0m" + payload)

            if payload not in vulnerable:
                vulnerable.append(payload)
            else:
                pass
        else:
            pass
    file.close()

    print("[-] Available payloads:")
    print("\n".join(vulnerable))
    ask_to_save = input("Do you want to save these payloads to a text file : ")
    if ask_to_save == "y" or ask_to_save == "Y" :
        print("Saving...")
        with open("Xss_Payloads_logs.txt" , 'a') as f:
             f.write("\n".join(vulnerable))
        f.close()
        
        print("Logs are saved in the current directory")
