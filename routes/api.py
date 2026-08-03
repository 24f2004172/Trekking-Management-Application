from flask import Blueprint, render_template, redirect, url_for, jsonify
from models.user import User
from flask import request

api = Blueprint('api', __name__)

@api.route("/trekker")
def trekker():
    user_trek = User.query.first()
    if not user_trek:
        return jsonify({"error": "no user found"}), 404

    data = {
        "id": user_trek.id,
        "name": user_trek.name,
        "email": user_trek.email,
        "phone": user_trek.phone,
        "role": user_trek.role
    }

    return jsonify(data)
