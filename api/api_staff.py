from datetime import timedelta, date
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from utils.decorators import role_required
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from extensions import db
from models.user import User
from models.trek import Trek
from models.booking import Booking
from models.staff_profile import StaffProfile

apiStaff = Blueprint('apiStaff', __name__)

@apiStaff.route('/dashboard')
@jwt_required()
@role_required('Staff')
def get_dashboard():
    staff_id = get_jwt_identity()
    staff_treks = Trek.query.filter_by(assigned_staff_id=staff_id)

    trek_data = []
    for trek in staff_treks:
        bookings = Booking.query.filter_by(trek_id = trek.id).count()

        data = {
            'id': trek.id,
            'trek_name': trek.trek_name,
            'total_slots': trek.total_slots,
            'available_slots': trek.available_slots,
            'status': trek.status,
            'registered_users': bookings
        }

        trek_data.append(data)

    return jsonify({
        "success": True,
        "message": "Trek data accessed successfully.",
        "data": trek_data
    }), 201

@apiStaff.route('/trek/<int:id>/participants')
@jwt_required()
@role_required('Staff')
def get_trek_participants(id):
    trek = Trek.query.get(id)

    if not trek:
        return jsonify({
            "success": False,
            "message": f"Invalid trek id: {id}"
        })

    staff_id = get_jwt_identity()

    if trek.assigned_staff_id != int(staff_id):
        return jsonify({
            "success": False,
            "message": "You are not assigned to this trek"
        }), 403

    bookings = Booking.query.filter_by(trek_id=trek.id)
    participants = []

    for booking in bookings:
        user_booked = User.query.get(booking.user_id)
        data = {
            'id': user_booked.id,
            'name': user_booked.name,
            'email': user_booked.email,
            'phone': user_booked.phone
        }

        participants.append(data)

    return jsonify({
            "success": True,
            "message": "Participants data accessed successfully.",
            "data": participants
        }), 201

@apiStaff.route('/trek/<int:id>/status', methods=['PUT'])
@jwt_required()
@role_required('Staff')
def put_status(id):
    data = request.get_json()
    trek = Trek.query.get(id)

    if not trek:
        return jsonify({
            "success": False,
            "message": f"Invalid trek id: {id}"
        })

    staff_id = get_jwt_identity()

    if trek.assigned_staff_id != int(staff_id):
        return jsonify({
            "success": False,
            "message": "You are not assigned to this trek"
        }), 403

    valid_status = ["Pending", "Approved", "Open", "Closed", "Completed"]

    if not data.get('status') or data.get('status') not in valid_status:
        return jsonify({
            "success": False,
            "message": f"Status is Invalid or not present"
        })

    trek.status = data.get('status')
    db.session.commit()

    return jsonify({
            "success": True,
            "message": "Status is updated successfully."
        }), 201
   