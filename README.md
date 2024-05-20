README for Microservice A
The instrucitons are included for how to request and recive the data using a RESTful API.
## Setup Instructions

### Prerequisites

Python 3.x
Flask
Flask SQLAlchemy
MySQL server

### Installation

1. Clone the repository:

    ```bash
    git clone <your-repo-url>
    cd <your-repo-directory>
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure your MySQL database connection in the `config.py` file:

    ```python
    SQLALCHEMY_DATABASE_URI = 'mysql://<username>:<password>@<host>:<port>/<database_name>'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ```

### Initialize the Database

Before running your application, initialize the MySQL database. In the same directory as `Blaine_microservice.py`, create an `initialize_db.py` file with the following content:

```python
from Blaine_microservice import app, db

with app.app_context():
    db.create_all()
```
or use an exisiting database and fill in the correct parts of the config.py file.

Here is an example of using the requests

Creating Audit Log Entries
Send a POST request to http://127.0.0.1:5000/audit-log-entry with JSON data containing the attributes of the audit log entry:

```json
{
  "action": "CREATE",
  "employee_id": 123,
  "record_type": "RESOURCE",
  "record_id": 456,
  "before_state": "{}",
  "after_state": "{}"
}


```
Retrieving Audit Log Entries
Send a GET request to http://127.0.0.1:5000/audit-log-entries to retrieve all audit log entries.

Retrieving Audit Log Entry by ID
Send a GET request to http://127.0.0.1:5000/audit-log-entry/<id> to retrieve a specific audit log entry by its ID.

Updating Audit Log Entries
Send a PUT request to http://127.0.0.1:5000/audit-log-entry/<id> with JSON data containing the updated attributes of the audit log entry:

```json
{
  "action": "UPDATE",
  "employee_id": 123,
  "record_type": "RESOURCE",
  "record_id": 456,
  "before_state": "{}",
  "after_state": "{}"
}
```

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

