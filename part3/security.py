from hmac import compare_digest
from part3.models.user import UserModel


def authenticate(username, password):
    """
    Function that gest called when user calls the auth endpoint with username and pwd.
    :param username: string format
    :param password: unencrypted pwd in string format
    :return: status of authentication i.e. success, none
    """
    user = UserModel.find_by_username(username)
    if user and compare_digest(user.password, password):
        return user


def identity(payload):
    """
    Function that gets called when user has already authenticated, and flask-jwt
    verifider their authorization header is correct
    :param payload: dictionary with 'identity' key
    :return: usermodel object
    """
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
