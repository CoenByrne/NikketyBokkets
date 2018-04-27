from src.models.User import UserConstants
from src.common.Database import Database
from src.common.Utils import Utils
import uuid


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def save_to_db(self):
        Database.insert(UserConstants.COLLECTION, self.json())

    def json(self):
        return {
            "_id": self._id,
            "email": self.email,
            "password": self.password
            }

    @staticmethod
    def register_user(email, password):
        """
        this method registers a user using e-mail and password.
        the password already comes hashed as sha-512.
        :param email: user's e-mail (might be invalid)
        :param password: sha512-hashed password
        :return: True if registered successfully, or False otherwise (exeptions can be raised)
        """

        user_data = Database.find_one(UserConstants.COLLECTION, {"email": email})

        if user_data is not None:
            return False
        if not Utils.email_is_valid(email):
            return False

        User(email, Utils.hash_password(password)).save_to_db()
        return True

    @staticmethod
    def login_user(email, password):
        user_data = Database.find_one(UserConstants.COLLECTION, {"email": email})

        if user_data is None:
            return False
        if not Utils.email_is_valid(email):
            return False

        if Utils.check_hashed_password(password, user_data['password']):
            return True
        else:
            return False

    @classmethod
    def find_by_email(cls, email):
        return cls(**Database.find_one(UserConstants.COLLECTION, {"email": email}))
