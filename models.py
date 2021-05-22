from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_login import UserMixin
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()
class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=50), nullable=False, unique=True)
    email_address = db.Column(db.String(length=100), nullable=False, unique=True)
    confirmed_email = db.Column(db.Boolean, nullable=False, default=False)
    password_hash = db.Column(db.String(length=60), nullable=False)

    def __repr__(self) -> str:
        return f'{self.username}'


    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)
