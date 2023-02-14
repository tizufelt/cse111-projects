import urllib.request
import http.client as httplib


def connect(host="http://google.com", timeout=3):
    connection = httplib.HTTPConnection(host,timeout=timeout)
    
    try:
        connection.request("HEAD", "/")
        connection.close()
        print()
        print("CONNECTED")
        print()
        return True
    except Exception as exep:
        print(exep)
        return False

connect("www.google.com", 3)
    
