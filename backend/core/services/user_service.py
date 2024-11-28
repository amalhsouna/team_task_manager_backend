from werkzeug.security import check_password_hash
from core.models.user import User  # Supposons que vous avez un modèle User avec SQLAlchemy

class UserService:
    @staticmethod
    def authenticate_user(username, password):
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):  # Vérifie le mot de passe
            return user
        return None

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    # @staticmethod
    # def create_user(username, password):
    #     """
    #     Crée un nouvel utilisateur.

    #     :param username: Nom d'utilisateur
    #     :param password: Mot de passe
    #     :return: L'utilisateur créé
    #     """
    #     hashed_password = generate_password_hash(password)
    #     new_user = User(username=username, password=hashed_password)
    #     db.session.add(new_user)
    #     db.session.commit()
    #     return new_user
