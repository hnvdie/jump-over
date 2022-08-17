import sys
import requests

def source(h):
    u = f"https://web.archive.org/cdx/search/cdx?url=*.{h}/*&output=list&fl=original&collapse=urlkey"
    r = requests.get(u).text
    if len(r) == 0:
       return "No result :)"
    return r

if __name__=="__main__":
   print("\n[waybackurls] - hnvdi3\n")
   if len(sys.argv) < 2 :
      sys.exit("\nwaybackurls.py <url> <output:optional>\ne.g: waybackurls.py google.com\nwaybackurls.py google.com result.txt\n")

   _ = source(sys.argv[1])
   if _:
      print(_)
      try:
        if sys.argv[2]:
           with open(sys.argv[2],"w") as f:
              f.write(_)
              print("[+] results saved at {}\n".format(sys.argv[2]))
              f.close()
      except IndexError:
        pass



