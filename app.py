from datetime import timedelta
from flask import Flask, jsonify, request
from extensions import db, jwt

from routes.main import main
from api.api import api


def create_app():
    app = Flask(__name__)
    app.secret_key = '24f2004172'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['JWT_SECRET_KEY'] = '24f2004172'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=8)

    jwt.init_app(app)
    db.init_app(app)
    app.register_blueprint(main)
    app.register_blueprint(api, url_prefix='/api')

    @app.before_request
    def handle_preflight():
        if request.method == 'OPTIONS':
            response = jsonify({})
            response.status_code = 200
            return response

    @app.after_request
    def add_cors_headers(response):
        origin = request.headers.get('Origin')
        allowed_origins = [
            'http://localhost:8080',
            'http://127.0.0.1:8080',
            'http://192.168.1.14:8080',
            'http://localhost:8081',
            'http://127.0.0.1:8081',
            'http://192.168.1.14:8081'
        ]

        if origin in allowed_origins:
            response.headers['Access-Control-Allow-Origin'] = origin
            response.headers['Access-Control-Allow-Credentials'] = 'true'
        else:
            response.headers['Access-Control-Allow-Origin'] = '*'

        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, PATCH, DELETE, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        return response

    with app.app_context():
        db.create_all()
        print('database created!')

    return app


app = create_app()


if __name__ == '__main__':
    app.run(debug=True)

