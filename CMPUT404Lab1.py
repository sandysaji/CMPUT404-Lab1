import requests
print(requests.__version__)

var = requests.get("https://raw.githubusercontent.com/sandysaji/CMPUT404-Lab1/master/CMPUT404Lab1.py")
print(var.content)