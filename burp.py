import requests

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = '{"application_logins":[{"password":"test","username":"test"}],"scan_configurations":[{"name":"Audit checks - light active","type":"NamedConfiguration"}],"urls":["https://example.com"]}'

response = requests.post('http://10.15.60.71:8080/api/b2TGb96QOhqBmD6KdFRPtiwZUnzlU5LX/v0.1/scan', headers=headers, data=data)
