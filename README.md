README for Microservice A
The instrucitons are included for how to request and recive the data using a RESTful API.
pip install Flask is required. 


## Requesting Data 

To create, read, or get specific audit log entries from the microservice, use the following endpoints:

#### Create an Audit Log Entry


**Request Body:**
```json
{
    "user_id": "user123",
    "action": "created",
    "details": "Created a new resource"
}
    }
}

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


import requests

entry_id = 1
response = requests.get(f'http://127.0.0.1:5000/audit-log-entries/{entry_id}')
print(response.json())

```
## Receiving Data
When you make requests to the endpoints, the microservice responds with JSON data. Here are examples of the responses:
```json
{
    "message": "Audit log entry created successfully",
    "entry": {
        "id": 1,
        "user_id": "user123",
        "action": "created",
        "details": "Created a new resource"
    }
}


[
    {
        "id": 1,
        "user_id": "user123",
        "action": "created",
        "details": "Created a new resource",
        "timestamp": "2024-05-19T15:20:30.123456"
    }
]

{
    "id": 1,
    "user_id": "user123",
    "action": "created",
    "details": "Created a new resource",
    "timestamp": "2024-05-19T15:20:30.123456"
}


```

How to Run the Microservice and Test Program
Start the Flask server:
python Blaine_microservice.py

test file
python test_client.py

