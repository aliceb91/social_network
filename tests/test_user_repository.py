from lib.user_repository import UserRepository
from lib.user import User

def test_pulls_user_list(db_connection):
    # Given a call of the all method
    # It returns a list of all current users.
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    users = repository.all()
    assert users == [
        User("Test username 1", "Test email address 1", 1),
        User("Test username 2", "Test email address 2", 2),
        User("Test username 3", "Test email address 3", 3),
        User("Test username 4", "Test email address 4", 4)
    ]

def test_creates_new_user(db_connection):
    # Given new user information
    # It adds this information to the database.
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    user = User("Test username 5", "Test email address 5")
    repository.create(user)
    users = repository.all()
    assert users == [
        User("Test username 1", "Test email address 1", 1),
        User("Test username 2", "Test email address 2", 2),
        User("Test username 3", "Test email address 3", 3),
        User("Test username 4", "Test email address 4", 4),
        User("Test username 5", "Test email address 5", 5)
    ]

def test_finds_specific_user(db_connection):
    # Given a user is
    # It returns the required User object.
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    user = repository.find(1)
    assert user == User("Test username 1", "Test email address 1", 1)
