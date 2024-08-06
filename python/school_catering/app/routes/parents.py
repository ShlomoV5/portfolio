from flask import Blueprint, request, jsonify
from app.models import db, User, Absence

parents_bp = Blueprint('parents', __name__)

@parents_bp.route('/absence', methods=['POST'])
def report_absence():
    data = request.json
    student_id = data.get('student_id')
    date = data.get('date')

    absence = Absence(student_id=student_id, date=date)
    db.session.add(absence)
    db.session.commit()

    return jsonify({'message': 'Absence reported successfully.'}), 201
