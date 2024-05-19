README for Microservice A
The instrucitons are included for how to request and recive the data using a RESTful API.
pip install Flask is required. 


## Communication Contract

### Requesting Data 

To create, read, or get specific audit log entries from the microservice, use the following endpoints:

#### Create an Audit Log Entry

**Endpoint:** `POST /audit-log-entries`

**Example Call:**

import requests

BASE_URL = 'http://127.0.0.1:5000/audit-log-entries'
payload = {
    'user_id': 'user123',
    'action': 'created',
    'details': 'Created a new resource'
}
response = requests.post(BASE_URL, json=payload)
print(response.json())


import requests

BASE_URL = 'http://127.0.0.1:5000/audit-log-entries'
response = requests.get(BASE_URL)
print(response.json())

Example Call
import requests

entry_id = 1
response = requests.get(f'http://127.0.0.1:5000/audit-log-entries/{entry_id}')
print(response.json())

Receiving Data
When you make requests to the endpoints, the microservice responds with JSON data. Here are examples of the responses:

{
    "message": "Audit log entry created successfully",
    "entry": {
        "id": 1,
        "timestamp": "2024-05-19T15:20:30.123456",
        "user_id": "user123",
        "action": "created",
        "details": "Created a new resource"
    }
}
