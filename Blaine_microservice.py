from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

class AuditLogEntry(db.Model):
    __tablename__ = 'audit_log_entries'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(255))
    action = db.Column(db.String(255))
    details = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, default=db.func.now())

@app.route('/')
def home():
    return 'Welcome to Blaine Microservice'

@app.route('/audit-log-entries')
def view_audit_log_entries():
    audit_log_entries = AuditLogEntry.query.all()
    entries = []
    for entry in audit_log_entries:
        entries.append({
            'id': entry.id,
            'user_id': entry.user_id,
            'action': entry.action,
            'details': entry.details,
            'timestamp': entry.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        })
    return jsonify(entries)

@app.route('/audit-log-entry', methods=['POST'])
def create_audit_log_entry():
    data = request.get_json()
    new_entry = AuditLogEntry(
        user_id=data['user_id'],
        action=data['action'],
        details=data['details']
    )
    db.session.add(new_entry)
    db.session.commit()
    return jsonify({'message': 'Audit log entry created'}), 201

@app.route('/audit-log-entry/<int:id>', methods=['PUT'])
def update_audit_log_entry(id):
    data = request.get_json()
    entry = AuditLogEntry.query.get(id)
    if not entry:
        return jsonify({'message': 'Entry not found'}), 404

    entry.user_id = data.get('user_id', entry.user_id)
    entry.action = data.get('action', entry.action)
    entry.details = data.get('details', entry.details)
    db.session.commit()
    return jsonify({'message': 'Audit log entry updated'})

@app.route('/audit-log-entry/<int:id>', methods=['GET'])
def get_audit_log_entry(id):
    entry = AuditLogEntry.query.get(id)
    if not entry:
        return jsonify({'message': 'Entry not found'}), 404

    return jsonify({
        'id': entry.id,
        'user_id': entry.user_id,
        'action': entry.action,
        'details': entry.details,
        'timestamp': entry.timestamp.strftime('%Y-%m-%d %H:%M:%S')
    })

if __name__ == '__main__':
    app.run(debug=True)
