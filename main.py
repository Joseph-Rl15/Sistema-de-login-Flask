from flask import Flask,render_template
from rotas.home import home_rota
from rotas.usuarios import usuario_route
from flask_sqlalchemy import SQLAlchemy
from database.usuarios import db

app = Flask(__name__)
app.secret_key = "123"


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app) 

app.register_blueprint(home_rota)
app.register_blueprint(usuario_route)



if __name__ == "__main__":
   with app.app_context():
    db.create_all()
    
    app.run(debug=True)





