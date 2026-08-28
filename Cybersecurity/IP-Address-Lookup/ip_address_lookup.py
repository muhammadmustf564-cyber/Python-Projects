import socket

site = input("Enter website: ")

try:
    ip = socket.gethostbyname(site)
    print("IP Address:", ip)
except socket.gaierror:
    print("Unable to find the IP address.")

