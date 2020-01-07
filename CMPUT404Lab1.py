import requests
print(requests.__version__)

var = requests.get("http://google.com/")
print(var.status_code)