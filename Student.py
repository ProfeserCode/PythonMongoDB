# Definition of the Student class
class Student:
    # Constructor method to initialize a Student instance with provided attributes
    def __init__(self, sid, username, email, year, department):
        # Assigning provided values to instance variables
        self.sid = sid
        self.username = username
        self.email = email
        self.year = year
        self.department = department

    # Class method to create a Student instance from user input
    @classmethod
    def from_user_input(cls):
        # Taking user input for each attribute
        sid = input("Enter StudentId: ")
        username = input("Enter Name: ")
        email = input("Enter Email: ")
        year = int(input("Enter Year: "))
        department = input("Enter Department: ")

        # Creating and returning a new Student instance with user-provided values
        return cls(sid, username, email, year, department)
