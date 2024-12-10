from flask import Flask
from routes import init_routes
from db.db_config import criar_tabelas_sqlalchemy

def create_app():
    app = Flask(__name__)

    criar_tabelas_sqlalchemy()

    init_routes(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
