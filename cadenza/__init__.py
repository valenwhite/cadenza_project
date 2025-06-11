#import flask - from the package import class
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.debug = True
    app.secret_key = 'MySecretKey'

    #set the app configuration data 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cadenza.sqlite'

    db.init_app(app)

    Bootstrap(app)

    from . import views
    app.register_blueprint(views.bp)

    @app.errorhandler(404)
    # takes error as parameter
    def not_found(e):
        return render_template("404.html", error=e)

    @app.errorhandler(500)
    # takes error as parameter
    def not_found(e):
        return render_template("500.html", error=e)

    return app 