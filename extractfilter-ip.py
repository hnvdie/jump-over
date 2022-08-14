
import sys
import socket
import time
from concurrent import futures

banner = """
simple python code for automation
extracting IP & filtering duplicates
from collected subdomains.
"""

help = """
usage
   -  python3 main.py <subdo_list> <output>

example
   -  python3 main targets.txt output.txt 
   -  python3 main targets.txt 
      (default output: results.txt)

"""

print(banner)
time.sleep(1.9)


try:
   targets = sys.argv[1]
   try:
      output = sys.argv[2]
   except:
      output = "results.txt"
except:
   sys.exit(help)


domains = []
for _ in open(sys.argv[1],'r'):
    _ = _.split()[0]
    domains.append(_)

def get(domain):
    try:
         host = socket.gethostbyname(domain)
         print (f"[\033[92m+\033[97m] {domain} -> \033[92m{host}\033[97m")
         return host
    except Exception as msg:
         print (f"[\033[91m-\033[97m] {domain} >> \033[91m{msg}\033[97m")
         return

def filter(lists):
    _ = []
    for __ in lists:
        if __ == None:
           pass
        elif __ not in _:
           _.append(__)
        else:pass
    return _

def write(IP,path=output):
    with open(path,"w") as f:
         for _ in IP:
           f.write(_+'\n')
         f.close()
    return path

def main():
    results = []
    with futures.ProcessPoolExecutor(max_workers=5) as f:
         res = [f.submit(get,domain) for domain in domains]
         for see in res:
             results.append(see.result())

    end = write(filter(results))
    return print("-"*40,f"\n[+] All done ~, output saved at {end}")



if __name__=="__main__":
   main()
