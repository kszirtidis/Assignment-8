from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///audit_log.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class AuditLogEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.String(50), nullable=False)
    action = db.Column(db.String(100), nullable=False)
    details = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<AuditLogEntry {self.id}>'

@app.route('/audit-log-entries', methods=['POST'])
def create_audit_log_entry():
    data = request.get_json()
    new_entry = AuditLogEntry(
        user_id=data['user_id'],
        action=data['action'],
        details=data.get('details')
    )
    db.session.add(new_entry)
    db.session.commit()
    return jsonify({"message": "Audit log entry created successfully", "entry": {
        "id": new_entry.id,
        "timestamp": new_entry.timestamp,
        "user_id": new_entry.user_id,
        "action": new_entry.action,
        "details": new_entry.details
    }}), 201

@app.route('/audit-log-entries', methods=['GET'])
def get_audit_log_entries():
    entries = AuditLogEntry.query.all()
    return jsonify([{
        "id": entry.id,
        "timestamp": entry.timestamp,
        "user_id": entry.user_id,
        "action": entry.action,
        "details": entry.details
    } for entry in entries])

@app.route('/audit-log-entries/<int:id>', methods=['GET'])
def get_audit_log_entry(id):
    entry = AuditLogEntry.query.get_or_404(id)
    return jsonify({
        "id": entry.id,
        "timestamp": entry.timestamp,
        "user_id": entry.user_id,
        "action": entry.action,
        "details": entry.details
    })

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
