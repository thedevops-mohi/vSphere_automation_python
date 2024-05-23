from pprint import pprint
import requests
import json
import time
import pandas as pd
import csv

import requests as requests

url = "https://[vsphere fqdn here]/rest/vcenter/vm/"

vmlist = []
vmid = []
vm_list = []
result = []
name   = {}
memory = {}
state  = {}
id     = {}
cpu    = {}

token_code = input("Please enter session token to authenticate:  ")
payload={}
headers = {
 'vmware-api-session-id': token_code,
 'Cookie': 'vmware-api-session-id=e1565115828422447465648242e0b713'
}

response = requests.request("GET", url, headers=headers, data=payload,verify=False)
api_date = response.json()
print(type(response))
print(api_date['value'])
for i in range(len(api_date['value'])):
    print(f"VM Name: {api_date['value'][i]['name']}")
    print(f"Memory Size (MB): {api_date['value'][i]['memory_size_MiB']}")
    print(f"VM ID: {api_date['value'][i]['vm']}")
    print(f"Power State: {api_date['value'][i]['power_state']}")
    print(f"CPU Count: {api_date['value'][i]['cpu_count']}")
    print('+'*50)
    name['name']      = api_date['value'][i]['name']
    memory['memory']  = api_date['value'][i]['memory_size_MiB']
    state['state']    = api_date['value'][i]['power_state']
    id['id']          = api_date['value'][i]['vm']
    cpu['cpu']        = api_date['value'][i]['cpu_count']
    vmid.append(name.values())
# for j in range(len(vmid)):
#     url = f"https://vcsa.mdeey.com/rest/vcenter/vm/{vmid[j]}"
#     payload = {}
#     headers = {
#         'vmware-api-session-id': 'e2b8c54091637896aaf1a68626bc7961',
#         'Cookie': 'vmware-api-session-id=e1565115828422447465648242e0b713'
#     }
#     response = requests.request("GET", url, headers=headers, data=payload, verify=False)
#     api_date = response.json()
#     result.append(api_date)
# print(result['value'])

time_str = time.strftime("%Y%m%d-%H%M%S")
header =['VM Name','Memory Size(MB)','VM ID','Power State','CPU Count']
filename = 'getVmList.csv'
with open(filename,'w',newline='') as csvfile:
    spawwriter = csv.writer(csvfile,delimiter=',',quoting=csv.QUOTE_MINIMAL)
    spawwriter.writerow(header)
    for i in vmid:
        spawwriter.writerow(vmid)


