import requests

URL = 'http://127.0.0.1:8000/create/'

data = {
    'name': 'Sameer',
    'roll': 48,
    'city': 'Lahore'
}

res = requests.post(URL, json=data)   # ✅ send JSON with correct headers
print("Status:", res.status_code)
print("Response:", res.json())
