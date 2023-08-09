class User():
    def __init__(self, username, email_address, id = None):
        # Assigns data for the user's username and email address
        #
        # Parameters:
        #   username: string
        #   email_address: string
        self.username = username
        self.email_address = email_address
        self.id = id

    def __eq__(self, other):
        # Compares the instance variables of these objects.
        return self.__dict__ == other.__dict__

    def __repr__(self):
        # Outputs the contents of the object as a string when the object is called.
        return f"{self.id}, {self.username}, {self.email_address}"
