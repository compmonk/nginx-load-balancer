import requests
from bs4 import BeautifulSoup
import sys


def parse_output(text):
  soup = BeautifulSoup(text, 'html.parser')
  return int(soup.title.string[-1])


# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
  """
  Call in a loop to create terminal progress bar
  @params:
    iteration   - Required  : current iteration (Int)
    total       - Required  : total iterations (Int)
    prefix      - Optional  : prefix string (Str)
    suffix      - Optional  : suffix string (Str)
    decimals    - Optional  : positive number of decimals in percent complete (Int)
    length      - Optional  : character length of bar (Int)
    fill        - Optional  : bar fill character (Str)
  """
  percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
  filledLength = int(length * iteration // total)
  bar = fill * filledLength + '-' * (length - filledLength)
  print("\r{0} |{1}| {2}% {3}".format(prefix, bar, percent, suffix), end = '\r')
  # Print New Line on Complete
  if iteration == total: 
    print()  


def main(server_address, visits = 2000, slaves = 4):
  loads = {}
  for slaves_no in range(1, slaves + 1):
    loads[slaves_no] = 0
  
  with requests.Session() as session:
    print("Making {0} visits for server address {1} with {2} slaves".format(visits, server_address, slaves))
    for _ in range(visits):
      response = session.get(server_address)
      slaves_no = parse_output(response.text)
      loads[slaves_no] += 1
      printProgressBar(_ + 1, visits, prefix = 'Progress:', suffix = 'Complete', length = 50)
  
  for i in range(1, slaves + 1):
    print("Server {0} visits: {1}".format(i, loads[i]))
  
  print("Total visits", sum(loads.values()))
    

if __name__ == '__main__':
  if len(sys.argv) == 2:
    server_address = sys.argv[1]
    main(server_address)
  else:
    print("Please provide server address")
