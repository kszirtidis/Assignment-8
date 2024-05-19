import requests

BASE_URL = 'http://127.0.0.1:5000/audit-log-entries'

def create_audit_log_entry(user_id, action, details):
    payload = {
        'user_id': user_id,
        'action': action,
        'details': details
    }
    response = requests.post(BASE_URL, json=payload)
    return response.json()

def get_audit_log_entries():
    response = requests.get(BASE_URL)
    return response.json()

def get_audit_log_entry(entry_id):
    response = requests.get(f'{BASE_URL}/{entry_id}')
    return response.json()

if __name__ == '__main__':
    print("Creating an audit log entry...")
    entry = create_audit_log_entry('user123', 'created', 'Created a new resource')
    print("Response:", entry)

    print("\nFetching all audit log entries...")
    entries = get_audit_log_entries()
    print("Response:", entries)

    print("\nFetching a specific audit log entry by ID...")
    if entries:
        entry_id = entries[0]['id']
        specific_entry = get_audit_log_entry(entry_id)
        print("Response:", specific_entry)
