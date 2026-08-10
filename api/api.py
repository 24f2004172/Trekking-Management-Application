from datetime import timedelta, date
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from utils.decorators import role_required
from utils.remainder_service import send_daily_reminders
from flask import render_template
from utils.report_service import generate_monthly_report

from extensions import db
from models.user import User
from models.trek import Trek
from models.booking import Booking
from models.staff_profile import StaffProfile

api = Blueprint('api', __name__)

#Route Register for the trekker
@api.route('/register', methods=['POST'])
def register():
    data = request.get_json(silent=True) or {}

    req_fields = ['name', 'email', 'password', 'phone']
    for field in req_fields:
        if not data.get(field):
            return jsonify({
                "success": False,
                "message": f"{field} is required."
            }), 400

    existing_user = User.query.filter_by(email=data["email"]).first()
    if existing_user:
        return jsonify({
            "success": False,
            "message": "Email already registered"
        }), 409

    hashed_password = generate_password_hash(data["password"])

    new_user = User(
        name=data["name"],
        email=data["email"],
        password=hashed_password,
        phone=data["phone"]
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Registration successful"
    }), 201


#Route login for the role based
@api.route("/login", methods=['POST'])
def login():
    data = request.get_json()

    req_fields = ['email', 'password']
    for field in req_fields:
        if not data.get(field):
            return jsonify({
                "success": False,
                "message": f"{field} is required."
            }), 400

    existing_user = User.query.filter_by(email=data["email"]).first()
    if not existing_user:
        return jsonify({
            "success": False,
            "message": "Invalid email or password"
        }), 409

    if not check_password_hash(existing_user.password, data['password']):
        return jsonify({
            "success": False,
            "message": "Invalid email or password"
        }), 409

    if not existing_user.is_active:
        return jsonify({
            "success": False,
            "message": "Your account has been deactivated"
        }), 403

    access_token = create_access_token(
        identity=str(existing_user.id),
        additional_claims={
            "role": existing_user.role
        },
        expires_delta=timedelta(hours=24)
    )

    return jsonify({
        "success": True,
        "message": "Login successful",
        "token": access_token,
        "user": {
            "id": existing_user.id,
            "name": existing_user.name,
            "email": existing_user.email,
            "role": existing_user.role
        }
    }), 200

@api.route("/profile")
@jwt_required()
def profile():

    current_user = get_jwt_identity()
    existing_user = User.query.get(current_user)
    if not existing_user:
        return jsonify({
            "success": False,
            "message": "No valid token"
        })

    return jsonify({
        "success": True,
        "message": "Access approved!"
    })

@api.route("/admin/dashboard")
@jwt_required()
@role_required("Admin")
def admin_dashboard():
    dashboard_data = {
        "total_treks": Trek.query.count(),
        "total_staff": User.query.filter_by(role="Staff").count(),
        "total_users": User.query.filter_by(role="Trekker").count(),
        "total_bookings": Booking.query.count()
    }

    return jsonify({
        "success": True,
        "message": "Dashboard data fetched successfully",
        "data": dashboard_data
    })

@api.route("/admin/treks")
@jwt_required()
@role_required("Admin")
def get_treks():
    all_treks = Trek.query.all()
    trek_data = [trek.to_dict() for trek in all_treks]

    return jsonify({
        "success": True,
        "message": "All trek data accessed.",
        "data": trek_data
    }), 200

@api.route("/admin/treks", methods=['POST'])
@jwt_required()
@role_required("Admin")
def post_trek():
    data = request.get_json()

    req_fields = ['trek_name', 'location', 'difficulty', 'duration', 'total_slots', 'available_slots', 'assigned_staff_id', 'start_date']
    for field in req_fields:
        if not data.get(field):
            return jsonify({
                "success": False,
                "message": f"{field} is required."
            }), 400

    if data.get('available_slots') > data.get('total_slots'):
        return jsonify({
            "success": False,
            "message": "Available_slot must less than total_slots"
        }), 400

    image_url = data.get('image_url', '/images/hampta.jpg')
    date_string = data.get('start_date')
    parsed_date = date.fromisoformat(date_string)
    
    if data.get('description'):
        if data.get('status'):
            new_trek = Trek(
                trek_name = data.get('trek_name'),
                location = data.get('location'),
                difficulty = data.get('difficulty'),
                duration = data.get('duration'),
                total_slots = data.get('total_slots'),
                available_slots = data.get('available_slots'),
                assigned_staff_id = data.get('assigned_staff_id'),
                start_date = parsed_date,
                description = data.get('description'),
                status = data.get('status'),
                image_url = image_url
            )
        else:
            new_trek = Trek(
                trek_name = data.get('trek_name'),
                location = data.get('location'),
                difficulty = data.get('difficulty'),
                duration = data.get('duration'),
                total_slots = data.get('total_slots'),
                available_slots = data.get('available_slots'),
                assigned_staff_id = data.get('assigned_staff_id'),
                start_date = parsed_date,
                description = data.get('description'),
                image_url = image_url
            )
    else:
        new_trek = Trek(
            trek_name = data.get('trek_name'),
            location = data.get('location'),
            difficulty = data.get('difficulty'),
            duration = data.get('duration'),
            total_slots = data.get('total_slots'),
            available_slots = data.get('available_slots'),
            assigned_staff_id = data.get('assigned_staff_id'),
            start_date = parsed_date,
            image_url = image_url
        )

    db.session.add(new_trek)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Trek data is uploaded successfully.",
    }), 201
    

@api.route("/admin/treks/<int:id>", methods=['PUT'])
@jwt_required()
@role_required("Admin")
def put_trek(id):
    data = request.get_json() or {}
    trek = Trek.query.get(id)

    if not trek:
        return jsonify({
            "success": False,
            "message": f"Trek id {id} is invalid."
        }), 404

    updatable_fields = {
        'trek_name', 'location', 'description', 'difficulty',
        'duration', 'total_slots', 'available_slots',
        'start_date', 'end_date', 'status', 'assigned_staff_id', 'image_url'
    }

    for field, value in data.items():
        if field not in updatable_fields:
            continue

        if field in {'start_date', 'end_date'} and value:
            setattr(trek, field, date.fromisoformat(value))
        else:
            setattr(trek, field, value)

    if trek.available_slots > trek.total_slots:
        return jsonify({
            "success": False,
            "message": "available_slots cannot exceed total_slots."
        }), 400

    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Trek updated successfully.",
        "data": trek.to_dict()
    }), 200


@api.route("/admin/treks/<int:id>", methods=['DELETE'])
@jwt_required()
@role_required("Admin")
def delete_trek(id):
    trek = Trek.query.get(id)

    if not trek:
        return jsonify({
            "success": False,
            "message": f"Trek id {id} is invalid."
        }), 404

    db.session.delete(trek)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Trek deleted successfully."
    }), 200

@api.route("/admin/staff")
@jwt_required()
@role_required("Admin")
def get_staff():
    all_staff = User.query.filter_by(role="Staff")
    staff_data = [staff.to_dict() for staff in all_staff]

    return jsonify({
        "success": True,
        "message": "All Staff data accessed.",
        "data": staff_data
    }), 200

@api.route("/admin/staff", methods=['POST'])
@jwt_required()
@role_required("Admin")
def post_staff():
    data = request.get_json()

    req_fields = ['name', 'email', 'password', 'phone']
    for field in req_fields:
        if not data.get(field):
            return jsonify({
                "success": False,
                "message": f"{field} is required."
            }), 400
    
    if data.get('is_active'):
        new_staff = User(
            name = data.get('name'),
            email = data.get('email'),
            password = data.get('password'),
            phone = data.get('phone'),
            role = 'Staff',
            is_active = data.get('is_active')
        )
    else:
        new_staff = User(
            name = data.get('name'),
            email = data.get('email'),
            password = data.get('password'),
            phone = data.get('phone'),
            role = 'Staff'
        )

    db.session.add(new_staff)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Staff data is uploaded successfully.",
    }), 201

@api.route("/admin/staff/<int:id>", methods=['PUT'])
@jwt_required()
@role_required("Admin")
def put_staff(id):
    data = request.get_json() or {}
    staff = User.query.get(id)

    if not staff:
        return jsonify({
            "success": False,
            "message": f"Staff id {id} is invalid."
        }), 404

    updatable_fields = {'name', 'email', 'phone','is_active'}

    for field, value in data.items():
        if field not in updatable_fields:
            continue

        setattr(staff, field, value)

    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Staff updated successfully.",
        "data": staff.to_dict()
    }), 200

@api.route("/admin/staff/<int:id>", methods=['DELETE'])
@jwt_required()
@role_required("Admin")
def delete_staff(id):
    staff = User.query.get(id)

    if not staff:
        return jsonify({
            "success": False,
            "message": f"Staff id {id} is invalid."
        }), 404

    db.session.delete(staff)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Staff deleted successfully."
    }), 200

@api.route("/admin/staff_profile/<int:id>")
@jwt_required()
@role_required("Admin")
def get_staff_profile(id):
    staff_profile = StaffProfile.query.get(user_id=id)

    if staff_profile:
        return jsonify({
                "success": True,
                "message": f"Staff_profile with id {id} accessed.",
                "data": staff_profile
            }), 200

    return jsonify({
            "success": False,
            "message": f"Staff_profile with id {id} is invalid.",
            "data": staff_profile
        }), 200

@api.route("/admin/staff_profile/<int:id>", methods=['PUT'])
@jwt_required()
@role_required("Admin")
def put_staff_profile(id):
    data = request.get_json() or {}
    staff_profile = StaffProfile.query.get(user_id=id)

    if not staff_profile:
        return jsonify({
            "success": False,
            "message": f"Staff_profile with id {id} is invalid."
        }), 404

    updatable_fields = {'designation', 'experience', 'emergency_contact','status'}

    for field, value in data.items():
        if field not in updatable_fields:
            continue

        setattr(staff_profile, field, value)

    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Staff_profile updated successfully."
    }), 200


@api.route("/admin/users")
@jwt_required()
@role_required("Admin")
def get_users():
    users = User.query.filter_by(role="Trekker")
    user_data = [user.to_dict() for user in users]

    return jsonify({
        "success": True,
        "message": "All User data accessed.",
        "data": user_data
    }), 200

@api.route("/admin/user/<int:id>", methods=['PUT'])
@jwt_required()
@role_required("Admin")
def put_user(id):
    data = request.get_json() or {}
    user = User.query.get(id)

    if not user:
        return jsonify({
            "success": False,
            "message": f"User id {id} is invalid."
        }), 404

    updatable_fields = {'is_active'}

    for field, value in data.items():
        if field not in updatable_fields:
            continue

        setattr(user, field, value)

    db.session.commit()

    return jsonify({
        "success": True,
        "message": "User status updated successfully.",
        "data": user.to_dict()
    }), 200

@api.route("/admin/bookings")
@jwt_required()
@role_required("Admin")
def get_bookings():
    bookings = Booking.query.all()
    booking_data = [booking.to_dict() for booking in bookings]

    return jsonify({
        "success": True,
        "message": "All booking data accessed.",
        "data": booking_data
    }), 200

@api.route("/admin/booking/<int:id>", methods=['PUT'])
@jwt_required()
@role_required("Admin")
def updata_status(id):
    data = request.get_json() or {}
    booking = Booking.query.get(id)

    if not booking:
        return jsonify({
            "success": False,
            "message": f"Booking id {id} is invalid."
        }), 404

    updatable_fields = {'booking_status', 'payment_status'}

    for field, value in data.items():
        if field not in updatable_fields:
            continue

        setattr(booking, field, value)

    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Booking status updated successfully.",
        "data": booking.to_dict()
    }), 200
    

#Daily Remainder route
@api.route("/admin/send-reminders")
@jwt_required()
@role_required("Admin")
def admin_send_reminders():

    count = send_daily_reminders()

    return jsonify({
        "success": True,
        "sent_count": count,
        "message": f"{count} user reminders sent"
    })

@api.route("/admin/monthly-report")
@jwt_required()
@role_required("Admin")
def monthly_report():

    data = generate_monthly_report()

    return render_template(
        "monthly_report.html",
        trek_count=data["trek_count"],
        participant_count=data["participant_count"],
        popular_treks=data["popular_treks"]
    )
