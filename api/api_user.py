from datetime import timedelta, date
from flask import Blueprint, request, jsonify, send_file
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from utils.decorators import role_required

from utils.export_service import export_booking_history

from extensions import db
from models.user import User
from models.trek import Trek
from models.booking import Booking
from models.notification import Notification
from models.staff_profile import StaffProfile

apiUser = Blueprint('apiUser', __name__)

@apiUser.route('/dashboard')
@jwt_required()
@role_required('Trekker')
def get_dashboard():

    user_id = get_jwt_identity()

    available_treks = Trek.query.filter(
        Trek.status == "Open",
        Trek.available_slots > 0
    ).limit(3).all()

    my_bookings = Booking.query.filter_by(
        user_id=user_id
    ).order_by(
        Booking.booking_date.desc()
    ).limit(5).all()

    # Quick Stats
    available_treks_count = Trek.query.filter(
        Trek.status == "Open",
        Trek.available_slots > 0
    ).count()

    active_bookings_count = Booking.query.filter(
        Booking.user_id == user_id,
        Booking.booking_status == "Booked"
    ).count()

    completed_treks_count = Booking.query.filter(
        Booking.user_id == user_id,
        Booking.booking_status == "Completed"
    ).count()

    return jsonify({
        "success": True,
        "data": {
            "stats": {
                "available_treks": available_treks_count,
                "active_bookings": active_bookings_count,
                "completed_treks": completed_treks_count
            },

            "available_treks_list": [
                trek.to_dict()
                for trek in available_treks
            ],

            "recent_bookings": [
                booking.to_dict()
                for booking in my_bookings
            ]
        }
    }), 200

@apiUser.route('/treks')
@jwt_required()
@role_required('Trekker')
def get_treks():

    search = request.args.get('search')
    difficulty = request.args.get('difficulty')
    location = request.args.get('location')

    query = Trek.query.filter(
        Trek.status == "Open",
        Trek.available_slots > 0
    )

    if search:
        query = query.filter(
            Trek.trek_name.ilike(f"%{search}%")
        )

    if difficulty:
        query = query.filter_by(
            difficulty=difficulty
        )

    if location:
        query = query.filter(
            Trek.location.ilike(f"%{location}%")
        )

    treks = query.all()

    return jsonify({
        "success": True,
        "data": [
            trek.to_dict()
            for trek in treks
        ]
    }), 200

@apiUser.route('/trek/<int:id>')
@jwt_required()
@role_required('Trekker')
def get_trek(id):

    trek = Trek.query.get(id)

    if not trek:
        return jsonify({
            "success": False,
            "message": "Trek not found"
        }), 404

    return jsonify({
        "success": True,
        "data": trek.to_dict()
    }), 200

@apiUser.route('/bookings', methods=['POST'])
@jwt_required()
@role_required('Trekker')
def create_booking():

    user_id = get_jwt_identity()

    data = request.get_json()

    trek_id = data.get('trek_id')
    people = data.get('number_of_people', 1)

    trek = Trek.query.get(trek_id)

    if not trek:
        return jsonify({
            "success": False,
            "message": "Invalid Trek"
        }), 404

    if trek.status != "Open":
        return jsonify({
            "success": False,
            "message": "Trek is closed"
        }), 400

    existing_booking = Booking.query.filter_by(
        user_id=user_id,
        trek_id=trek_id
    ).first()

    if existing_booking:
        return jsonify({
            "success": False,
            "message": "Already booked"
        }), 400

    if trek.available_slots < people:
        return jsonify({
            "success": False,
            "message": "Not enough slots"
        }), 400

    booking = Booking(
        user_id=user_id,
        trek_id=trek_id,
        number_of_people=people
    )

    trek.available_slots -= people

    db.session.add(booking)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Booking successful"
    }), 201

@apiUser.route('/bookings')
@jwt_required()
@role_required('Trekker')
def get_bookings():

    user_id = get_jwt_identity()

    bookings = Booking.query.filter_by(
        user_id=user_id
    ).all()

    return jsonify({
        "success": True,
        "data": [
            booking.to_dict()
            for booking in bookings
        ]
    }), 200

@apiUser.route('/booking/<int:id>/cancel')
@jwt_required()
@role_required('Trekker')
def cancel_booking(id):
    user_id = get_jwt_identity()

    booking = Booking.query.filter_by(
        id=id,
        user_id=user_id
    ).first()

    if not booking:
        return jsonify({
            "success": False,
            "message": "Booking not found"
        }), 404

    if booking.booking_status != "Booked":
        return jsonify({
            "success": False,
            "message": "Only booked treks can be cancelled"
        }), 400

    trek = Trek.query.get(booking.trek_id)

    trek.available_slots += booking.number_of_people

    booking.booking_status = "Cancelled"
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Booking cancelled successfully"
    }), 200

@apiUser.route('/history')
@jwt_required()
@role_required('Trekker')
def get_history():

    user_id = get_jwt_identity()

    bookings = Booking.query.join(Trek).filter(
        Booking.user_id == user_id,
        Booking.booking_status == "Completed",
        Trek.status == "Completed"
    ).all()

    return jsonify({
        "success": True,
        "data": [
            booking.to_dict()
            for booking in bookings
        ]
    }), 200

@apiUser.route('/profile')
@jwt_required()
@role_required('Trekker')
def get_profile():

    user = User.query.get(
        get_jwt_identity()
    )

    return jsonify({
        "success": True,
        "data": user.to_dict()
    }), 200

@apiUser.route('/profile', methods=['PUT'])
@jwt_required()
@role_required('Trekker')
def update_profile():

    user = User.query.get(
        get_jwt_identity()
    )

    data = request.get_json()

    user.name = data.get(
        "name",
        user.name
    )

    user.phone = data.get(
        "mobile",
        user.phone
    )

    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Profile updated"
    }), 200


#Export api
@apiUser.route("/export-history")
@jwt_required()
@role_required('Trekker')
def export_history():

    user_id = get_jwt_identity()

    filename = export_booking_history(user_id)

    notification = Notification(
        user_id=user_id,
        message="Your booking history CSV has been generated."
    )

    db.session.add(notification)
    db.session.commit()

    return send_file(
        filename,
        as_attachment=True
    )

@apiUser.route("/notifications")
@jwt_required()
@role_required('Trekker')
def notifications():

    user_id = get_jwt_identity()

    data = Notification.query.filter_by(
        user_id=user_id
    ).order_by(
        Notification.created_at.desc()
    ).all()

    return jsonify([
        {
            "id": n.id,
            "message": n.message,
            "is_read": n.is_read
        }
        for n in data
    ])


@apiUser.route("/notifications/<int:notification_id>/read", methods=["PATCH"])
@jwt_required()
@role_required('Trekker')
def mark_notification_as_read(notification_id):

    user_id = get_jwt_identity()

    notification = Notification.query.filter_by(
        id=notification_id,
        user_id=user_id
    ).first()

    if not notification:
        return jsonify({"message": "Notification not found"}), 404

    notification.is_read = True
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Notification marked as read"
    })
