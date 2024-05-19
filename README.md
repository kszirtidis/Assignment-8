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
Edit config file with correct database login and password.
Start the Flask server:
python Blaine_microservice.py

test file
python test_client.py


## Communication Contract

For which teammate did you implement “Microservice A”?
Blaine

What is the current status of the microservice? Hopefully, it’s done!

It is complete and worked during testing.

If the microservice isn’t done, which parts aren’t done and when will they be done?

N/A

How is your teammate going to access your microservice? Should they get your code from GitHub? Should they run your code locally? Is your microservice hosted somewhere? Etc.

There is a repo on github with the program the link will be provided.

If your teammate cannot access/call YOUR microservice, what should they do? Can you be available to help them? What’s your availability?

Please let me know as soon as possible so I may have time to fix it. I will be available as much as possible outside work hours.

If your teammate cannot access/call your microservice, by when do they need to tell you?

Preferably as soon as they found out something is not working so I can have it fixed to them as soon as I am able to get home and work on it. At least 2 days before they need it.

Is there anything else your teammate needs to know? Anything you’re worried about? Any assumptions you’re making? Any other mitigations / backup plans you want to mention or want to discuss with your teammate?

I am assuming they are using some kind of SQL database I am a bit worried how SQLAlchemy will work with it, but it should run well. 

