import requests

BASE_URL = 'http://127.0.0.1:5000'

def test_create_audit_log_entry():
    endpoint = '/audit-log-entries'
    data = {
        'user_id': 'user123',
        'action': 'created',
        'details': 'Created a new resource'
    }
    response = requests.post(BASE_URL + endpoint, json=data)
    print("Create Audit Log Entry Response:", response.json())

def test_get_all_audit_log_entries():
    endpoint = '/audit-log-entries'
    response = requests.get(BASE_URL + endpoint)
    print("Get All Audit Log Entries Response:", response.json())

def test_get_specific_audit_log_entry(entry_id):
    endpoint = f'/audit-log-entries/{entry_id}'
    response = requests.get(BASE_URL + endpoint)
    print(f"Get Specific Audit Log Entry (ID={entry_id}) Response:", response.json())

if __name__ == '__main__':
    # Test creating an audit log entry
    print("Testing creating an audit log entry...")
    test_create_audit_log_entry()

    # Test getting all audit log entries
    print("\nTesting getting all audit log entries...")
    test_get_all_audit_log_entries()

    # Test getting a specific audit log entry
    entry_id = 4  # Replace with the ID of the audit log entry you want to retrieve
    print(f"\nTesting getting a specific audit log entry (ID={entry_id})...")
    test_get_specific_audit_log_entry(entry_id)

