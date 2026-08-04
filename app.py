from flask import Flask
from extensions import db, jwt

from routes.main import main
from api.api import api

def create_app():
    app = Flask(__name__)
    app.secret_key = '24f2004172'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config["JWT_SECRET_KEY"] = "24f2004172"

    jwt.init_app(app)
    db.init_app(app)
    app.register_blueprint(main)
    app.register_blueprint(api, url_prefix='/api')

    with app.app_context():
        db.create_all()
        print('database created!')

    return app


app = create_app()


if __name__ == '__main__':
    app.run(debug=True)

