# Importing the 'Student' class from the 'Student' module
from Student import Student
# Importing the 'DatabaseManager' class from the 'DatabaseManager' module
from DatabaseManager import DatabaseManager

# Creating an instance of the DatabaseManager class
database = DatabaseManager()


# Main function for the program
def main():
    # Infinite loop to keep the program running until the student chooses to exit
    while True:
        # Printing menu options for the student
        print("Option:")
        print("Press [1] for insert a student.")
        print("Press [2] for show all the students.")
        print("Press [3] for show specific student.")
        print("Press [4] for update a student.")
        print("Press [5] for delete a student.")
        print("Press [6] for exit.")

        try:
            # Taking student input for their choice
            choice = int(input("Action: "))

            # Handling different choices made by the student
            if choice == 1:
                # Taking input for student details
                student = Student.from_user_input()
                # Inserting the student into the database
                database.insert(student)

            elif choice == 2:
                # Fetching all students' data from the database
                data = database.fetch_all()
                for student in data:
                    print(student)

            elif choice == 3:
                # Showing details of a specific student based on their ID
                sid = input("Enter the StudentId: ")
                data = database.fetch_one(sid)
                if data is None:
                    print("This is not present in the database!")
                else:
                    print(data)

            elif choice == 4:
                # Updating details of a specific student based on their ID
                sid = input("Enter the StudentId: ")
                updated_student = Student.from_user_input()
                # Updating the student in the database
                database.update(sid, updated_student)
                print("Student update successfully!")

            elif choice == 5:
                # Deleting a specific student based on their ID
                sid = input("Enter the StudentId: ")
                database.delete(sid)
                print("Student deleted successfully!")

            elif choice == 6:
                # Exiting the program
                break
            else:
                # Handling invalid choices
                print("Invalid option key! Please try again!")

        except Exception as e:
            # Handling exceptions and displaying an error message
            print(e)
            print("Invalid student! Please try again!")


# Entry point of the program
if __name__ == "__main__":
    # Calling the main function when the script is executed
    main()
