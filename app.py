from flask import Flask, render_template, request, flash, redirect, url_for
from flask_moment import Moment
from flask_migrate import Migrate
import logging
from logging import Formatter, FileHandler

from models import db


app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')

#db.init_app(app)


#migrate = Migrate(app, db)

@app.route('/')
def index():
    return "<h1>Hello</h1>"


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

if __name__ == '__main__':
    app.run()
