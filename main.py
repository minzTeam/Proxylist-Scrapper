import requests, json

country = "ID" #COUNTRY PROXY
limit = "20" #LIMIT PROXY LIST
link = "https://proxylist.geonode.com/api/proxy-list?limit="+limit+"&page=1&sort_by=lastChecked&sort_type=desc&country="+country
data = requests.get(link).text
fix = json.loads(data)
result = {
    "result": {
        "Region": country,
        "proxylist": []
    }
}
for x in fix["data"]:
    ip = x["ip"]
    port = x["port"]
    result["result"]["proxylist"].append(ip+":"+port)
print(str(json.dumps(result,indent=4)))
