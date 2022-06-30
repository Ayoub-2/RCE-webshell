# About this project 
This tool helps you turn an rce throught url parameter to turn into an interactive shell using python


## Installation 

```bash
$ git clone https://github.com/Ayoub-2/RCE-webshell.git
$ cd RCE-webshell
$ pip install -r requirements
$ python rce.py --help
```

to set up a lab : 
```bash
# on linux
$ cd docker-example
$ chmod +x build.sh
$ ./build.sh 
# on windows Powershell
$ cd docker-example
$ ./build.ps1
``` 

## Manual

``` 
$ python .\rce.py -h

 /$$$$$$$   /$$$$$$  /$$$$$$$$ /$$   /$$                /$$        /$$$$$$
| $$__  $$ /$$__  $$| $$_____/|__/  | $$              /$$$$       /$$$_  $$
| $$  \ $$| $$  \__/| $$       /$$ /$$$$$$ /$$    /$$|_  $$      | $$$$\ $$
| $$$$$$$/| $$      | $$$$$   | $$|_  $$_/|  $$  /$$/  | $$      | $$ $$ $$
| $$__  $$| $$      | $$__/   | $$  | $$   \  $$/$$/   | $$      | $$\ $$$$
| $$  \ $$| $$    $$| $$      | $$  | $$ /$$\  $$$/    | $$      | $$ \ $$$
| $$  | $$|  $$$$$$/| $$$$$$$$| $$  |  $$$$/ \  $/    /$$$$$$ /$$|  $$$$$$/
|__/  |__/ \______/ |________/|__/   \___/    \_/    |______/|__/ \______/ by:ayoub-2

usage: RCEit [-p [param]] [-x [path]] [-h] [url]

RCE to web Shell

positional arguments:
  url                   Url of the target

optional arguments:
  -p [param], --parametre [param]
                        parametre leading to rce , defaull cmd
  -x [path], --xpath [path]
                        The xpath including the result of a command
  -h, --help            show this help message and exit
```

</br>

### Thanks : 

erseco
