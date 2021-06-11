"""
Do not recode this source code.
Appreciate developer create it

URL Checker V1.0
Enjoy use my tools^_^
"""
import requests, datetime, os
from concurrent.futures import ThreadPoolExecutor
header = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36"}
ses = requests.Session()

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def banner():
    print("""
    _   _ ____  _        ____ _               _             
   | | | |  _ \| |      / ___| |__   ___  ___| | _____ _ __ 
   | | | | |_) | |     | |   | '_ \ / _ \/ __| |/ / _ \ '__|
   | |_| |  _ <| |___  | |___| | | |  __/ (__|   <  __/ |   
    \___/|_| \_\_____|  \____|_| |_|\___|\___|_|\_\___|_|v1.0

    Coder by https://satria-rahmat.herokuapp.com
    """)

def time():
    return str(datetime.datetime.now())[11:19]
live = 0
def check(url, save_path):
  global live
  resp_code = ses.get(url, headers=header).status_code
  if resp_code == 200:
    with open(save_path, "a") as save:
      save.write(url+"\n")
    live+=1
    print (url+" >> "+"valid")
  elif resp_code == 404:
    print (url+" >> "+"invalid")
  else:
    print (url+" >> "+"unknown")

def main():
  clr()
  banner()
  url_list = open(input(" Url list txt: "), "r").read().splitlines()
  save_path = input(' Save result to : ')
  if '.txt' not in save_path: save_path+='.txt'
  num_start = input(" Start number: ")
  num_end = input(" End number: ")
  maks = int(input(" Max workers : "))*7
  if maks < 500: maks = 500
  num_length = len(num_start)
  dom_list = [[f"{x}{str(int(num_start)+y).zfill(num_length)}.csv" for y in range(int(num_start), int(num_end)+1)] for x in url_list]
  total = len(dom_list)*len(dom_list[0])
  urls = []
  tStart = time()
  for x in dom_list:
    for y in x:
        if y == "": continue
        urls.append(y)

  with ThreadPoolExecutor(max_workers=maks) as pool:
    for domain in urls:
      pool.submit(check, domain, save_path)
  print("\nResult :\nLive : "+str(live)+'\nDie : '+str(total-live)+'Total : '+str(total))
  print('___________________\n\nStart : '+tStart+'End : '+time())

if __name__ == "__main__":
  main()
