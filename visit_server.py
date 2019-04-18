import requests
from bs4 import BeautifulSoup
import sys

def parse_output(text):
  soup = BeautifulSoup(text, 'html.parser')
  return int(soup.title.string[-1])

  

def main(server_address, visits = 2000, servers = 4):
  loads = {}
  for server_no in range(1, servers + 1):
    loads[server_no] = 0
  

  with requests.Session() as session:
    for _ in range(visits):
      response = session.get(server_address)
      server_no = parse_output(response.text)
      loads[server_no] += 1
  

  for i in range(1, servers + 1):
    print("Server {0} visits: {1}".format(i, loads[i]))
  
  print("Total visits", sum(loads.values()))
    

if __name__ == '__main__':
  if len(sys.argv) == 2:
    server_address = sys.argv[1]
    main(server_address)
  else:
    print("Please provide server address")
