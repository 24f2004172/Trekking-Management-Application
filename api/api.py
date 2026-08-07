from datetime import timedelta
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from utils.decorators import role_required

from extensions import db
from models.user import User
from models.trek import Trek

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
        expires_delta=timedelta(hours=8)
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
    return jsonify({
        "success": True,
        "message": "Dashboard data fetched successfully",
        "data": {
            "total_treks": 12,
            "total_staff": 5,
            "total_users": 150,
            "total_bookings": 72
        }
    })

@api.route("/admin/treks")
@jwt_required()
@role_required("Admin")
def get_treks():
    all_treks = Trek.query.all()

    return jsonify({
        "success": True,
        "message": "All trek data accessed.",
        "data": all_treks
    })

@api.route("/admin/treks", methods=['POST'])
@jwt_required()
@role_required("Admin")
def post_trek():
    data = request.get_json()
    print(data)

@api.route("/admin/treks/<id>", methods=['PUT'])
@jwt_required()
@role_required("Admin")
def put_trek():
    data = request.get_json()
    print(data)

@api.route("/admin/treks/<id>", methods=['DELETE'])
@jwt_required()
@role_required("Admin")
def delete_trek():
    id = request.args.get(id) or 0
    print(id)


@api.route("/staff/dashboard")
@jwt_required()
@role_required("Staff")
def staff_dashboard():

    return jsonify({
        "message": "Welcome Staff"
    })

@api.route("/trekker/dashboard")
@jwt_required()
@role_required("Trekker")
def trekker_dashboard():

    return jsonify({
        "message": "Welcome Trekker"
    })