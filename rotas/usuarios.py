from flask import Blueprint, render_template,request
from database.usuarios import Usuarios, db
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask import flash, redirect, url_for, session

usuario_route = Blueprint("usuarios", __name__)

@usuario_route.route("/", methods=['GET', 'POST'])
def login():
    
    if request.method == "POST":
        
        email = request.form.get("email").strip()
        senha = str(request.form.get("senha").strip())

        if not email or not senha:
            flash("Por favor preencha os campos", "danger")
            return redirect(url_for('usuarios.login'))
        
        usuario = Usuarios.query.filter_by(email=email).first()
        
        if usuario and check_password_hash(usuario.senha, senha):
            session['usuario_id'] = usuario.id
            session['usuario_email'] = usuario.email
            flash("Login feito com sucesso !! ", "success")
            return redirect(url_for('usuarios.sucesso'))
        
        flash("email ou senha estão incorretas ! ", "danger")
        return redirect(url_for('usuarios.login'))
        
        


    return render_template("index.html")
@usuario_route.route("/cadastrar", methods=['GET', 'POST'])
def cadastro():
    if request.method == "POST":
        
        email = request.form.get("email").strip()
        senha = request.form.get("senha").strip()

        if not email or not senha:
            flash("Por favor preencha os campos", "danger")
            return redirect(url_for('usuarios.cadastro'))
        
        usuario_existe = Usuarios.query.filter_by(email=email).first()

        if usuario_existe:
            flash("Ja temos um cadastro com este email !", "danger")
            return redirect(url_for('usuarios.cadastro'))
        
        senha_hash = generate_password_hash(senha)


        novo_usuario = Usuarios(
            email=email,
            senha=senha_hash,
            )
        db.session.add(novo_usuario)
        db.session.commit()
        
        flash("Conta criada com sucesso!", "success")
        return redirect(url_for('usuarios.login'))
    
    return render_template("cadastrar.html")


@usuario_route.route("/bemvindo")
def sucesso():
    return render_template("bem_vindo.html")