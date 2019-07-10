import requests

url = "https://animal-monitoring-system.firebaseio.com/.json"
payload = {"one": "Hello00000 from python auth",
           "two": "Everyon000000000000e from python auth"}

r = requests.post(url, json=payload)
print(r.status_code, r.reason)
