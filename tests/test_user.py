from lib.user import User

def test_makes_new_user():
    # Given a username and email address
    # It creates a User object containing this data.
    user = User("Hello", "hello@hello.hello", 1)
    assert user.id == 1
    assert user.username == "Hello"
    assert user.email_address == "hello@hello.hello"

def test_compares_contents():
    # Given two User objects
    # Compares the contents of these objects.
    user_1 = User("Hello", "hello@hello.hello", 1)
    user_2 = User("Hello", "hello@hello.hello", 1)
    assert user_1 == user_2

def test_return_contents():
    # Given a User object
    # It returns a string of it's contents.
    user = User("Hello", "hello@hello.hello", 1)
    assert str(user) == "1, Hello, hello@hello.hello"
