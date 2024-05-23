from pprint import pprint
import requests
import json
import time
import pandas as pd

print('*'*100)
fqdn_ip = input("Enter the IP or FQDN of Vcenter you wish to connect to: ")
url = f"https://{fqdn_or_ip}/rest/vcenter/vm/"

name_list = []
memory_list = []
state_list = []
id_list = []
cpu_list = []

token_code = input("Please enter session token to authenticate:  ")
payload={}
headers = {
    'vmware-api-session-id': token_code,
    'Cookie': 'vmware-api-session-id=e1565115828422447465648242e0b713'
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)
api_data = response.json()
print(api_data)
for i in range(len(api_data['value'])):
    print(f"VM Name: {api_data['value'][i]['name']}")
    print(f"Memory Size (MB): {api_data['value'][i]['memory_size_MiB']}")
    print(f"VM ID: {api_data['value'][i]['vm']}")
    print(f"Power State: {api_data['value'][i]['power_state']}")
    print(f"CPU Count: {api_data['value'][i]['cpu_count']}")
    print('+'*50)

    name_list.append(api_data['value'][i]['name'])
    memory_list.append(api_data['value'][i]['memory_size_MiB'])
    state_list.append(api_data['value'][i]['power_state'])
    id_list.append(api_data['value'][i]['vm'])
    cpu_list.append(api_data['value'][i]['cpu_count'])
    
    number_vms_powered_on = state_list.count('POWERED_ON')
    number_vms_powered_off = state_list.count('POWERED_OFF')
    number_vms = len(name_list)
    
    print("Number of VM:"+" "+ str(number_vms) + "\nNumber of VM Powered Off:" +" "+ str(number_vms_powered_off)+ "\nNumber of VM Powered On:" + " " + str(number_vms_powered_on))

# Create a DataFrame
    df = pd.DataFrame({
        'VM Name': name_list,
        'Memory': memory_list,
        'State': state_list,
        'ID': id_list,
        'CPU': cpu_list,
    })

# Export DataFrame to Excel
df.to_excel('vm_list.xlsx', index=False,sheet_name='VMs')