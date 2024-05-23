import requests

url = "https://vcsa.mdeey.com/rest/com/vmware/cis/session"
creds = {"username":"administrator@vsphere.local","password":"[vsphere password here]"}
payload={}
headers = {
  'Authorization': 'Basic YWRtaW5pc3RyYXRvckB2c3BoZXJlLmxvY2FsOkBQc2V1ZG9jb2RlMQ==',
  'Cookie': 'vmware-api-session-id=e1565115828422447465648242e0b713'
}

response = requests.request("POST", url, headers=headers, data=payload, auth=(creds['username'],creds['password']),verify=False)

print(response.text)