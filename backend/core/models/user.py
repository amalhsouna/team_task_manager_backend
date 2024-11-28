from werkzeug.security import generate_password_hash, check_password_hash

from core import database as db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)  # Hashé avec werkzeug
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def __repr__(self):
        return f"<User(email={self.email})>"

    def set_password(self, password):
        """
        Hash le mot de passe et le stocke.
        """
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """
        Vérifie si le mot de passe correspond au hash.
        """
        return check_password_hash(self.password, password)
