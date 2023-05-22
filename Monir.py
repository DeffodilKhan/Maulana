import socket
import pyfiglet
from termcolor import colored
Banner = colored(pyfiglet.figlet_format('Domain_Name'), 'yellow')
print(Banner)
Domain_Name = input("input your Domain:")
ip = socket.gethostbyname(Domain_Name)
print(ip)
