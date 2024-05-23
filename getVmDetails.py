from pprint import pprint
import requests
import json
import time
import csv

url = "https://[vshere fqdn here]/rest/vcenter/vm/[VM ID here]]"

vmlist = []
payload={}
headers = {
 'vmware-api-session-id': '4e1dbddeb088b943bebfe915360c8d0c',
 'Cookie': 'vmware-api-session-id=e1565115828422447465648242e0b713'
}

response = requests.request("GET", url, headers=headers, data=payload,verify=False)
api_date = response.json()
print(type(response))

print(api_date['value'])



