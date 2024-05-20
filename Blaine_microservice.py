from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

class AuditLogEntry(db.Model):
    __tablename__ = 'audit_log_entries'
    id = db.Column(db.Integer, primary_key=True)
    action = db.Column(db.Integer)
    employee_id = db.Column(db.Integer)
    record_type = db.Column(db.String(50))
    record_id = db.Column(db.Integer)
    before_state = db.Column(db.Text)
    after_state = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.now())

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
            'action': entry.action,
            'employee_id': entry.employee_id,
            'record_type': entry.record_type,
            'record_id': entry.record_id,
            'before_state': entry.before_state,
            'after_state': entry.after_state,
            'created_at': entry.created_at.strftime('%Y-%m-%d %H:%M:%S')
        })
    return jsonify(entries)

@app.route('/audit-log-entry', methods=['POST'])
def create_audit_log_entry():
    data = request.get_json()
    new_entry = AuditLogEntry(
        action=data['action'],
        employee_id=data['employee_id'],
        record_type=data['record_type'],
        record_id=data['record_id'],
        before_state=data['before_state'],
        after_state=data['after_state']
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

    entry.action = data.get('action', entry.action)
    entry.employee_id = data.get('employee_id', entry.employee_id)
    entry.record_type = data.get('record_type', entry.record_type)
    entry.record_id = data.get('record_id', entry.record_id)
    entry.before_state = data.get('before_state', entry.before_state)
    entry.after_state = data.get('after_state', entry.after_state)
    db.session.commit()
    return jsonify({'message': 'Audit log entry updated'})

@app.route('/audit-log-entry/<int:id>', methods=['GET'])
def get_audit_log_entry(id):
    entry = AuditLogEntry.query.get(id)
    if not entry:
        return jsonify({'message': 'Entry not found'}), 404

    return jsonify({
        'id': entry.id,
        'action': entry.action,
        'employee_id': entry.employee_id,
        'record_type': entry.record_type,
        'record_id': entry.record_id,
        'before_state': entry.before_state,
        'after_state': entry.after_state,
        'created_at': entry.created_at.strftime('%Y-%m-%d %H:%M:%S')
    })

if __name__ == '__main__':
    app.run(debug=True)
