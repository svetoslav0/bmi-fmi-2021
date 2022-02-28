import requests
 
server = "https://rest.ensembl.org"
ext = "/genetree/id/ENSGT00390000003602?sequence=none"
 
r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
 
if not r.ok:
  r.raise_for_status()
 
decoded = r.text

print(r.json()['tree']['events'])