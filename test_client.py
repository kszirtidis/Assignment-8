import requests
import json

BASE_URL = "http://127.0.0.1:5000"

def create_audit_log_entry(user_id, action, details):
    data = {
        "user_id": user_id,
        "action": action,
        "details": details
    }
    response = requests.post(f"{BASE_URL}/audit-log-entry", json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    return response.json()

def get_audit_log_entries():
    response = requests.get(f"{BASE_URL}/audit-log-entries")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    return response.json()

def get_audit_log_entry_by_id(entry_id):
    response = requests.get(f"{BASE_URL}/audit-log-entry/{entry_id}")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    return response.json()

def update_audit_log_entry(entry_id, user_id, action, details):
    data = {
        "user_id": user_id,
        "action": action,
        "details": details
    }
    response = requests.put(f"{BASE_URL}/audit-log-entry/{entry_id}", json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    return response.json()

# Create a new audit log entry
print("Creating audit log entry...")
create_response = create_audit_log_entry("user123", "CREATE", "Created a new resource")
print(create_response)

# Get all audit log entries
print("Fetching all audit log entries...")
entries = get_audit_log_entries()
print(entries)

# Get audit log entry by ID
print("Fetching audit log entry by ID...")
if entries:
    first_entry_id = entries[0]['id']
    entry = get_audit_log_entry_by_id(first_entry_id)
    print(entry)

    # Update the audit log entry
    print("Updating audit log entry...")
    update_response = update_audit_log_entry(first_entry_id, "user123", "UPDATE", "Updated the resource")
    print(update_response)
