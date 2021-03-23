user = {"username": "jose", "access_level": "guest"}


def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function


@make_secure ## prevent the function from being created as is and instead it will create it and pass it through the decorator
def get_admin_password():
    return "1234"

# get_admin_password = make_secure(get_admin_password) ## changed to @make_secure 
print(get_admin_password())
print(get_admin_password.__name__)


# -- keeping function name and docstring --
import functools


user = {"username": "jose", "access_level": "guest"}


def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function


@make_secure
def get_admin_password():
    return "1234"

print(get_admin_password())
print(get_admin_password.__name__)