''' Imports SQLite3 so that I can use the database (school.db) in my program  '''
import sqlite3  # imported to be able to use sql queries
import webbrowser  # imported to be able to open websites from this program
import pandas as pd  # imported to display databases, read sql queries
from choices import StudentAction, TeacherAction
from admin_commands import Student, Teacher  # explained in file
from admin_commands_2 import Course

pd.options.display.max_columns = None  #To remove restraints on the number
pd.options.display.max_rows = None     #of rows and columns that 'pandas' displays

connection = sqlite3.connect(
    "school.db"
)  # To connect to the database conataining all the data
   #(Students, Teachers, Courses, Enrollment,  Attendance, Grades)
cursor = connection.cursor()  # Just to make it easier to type

view_Courses = pd.read_sql_query(
    "SELECT * from Courses", connection
)  # View every single course in the database

stva1 = pd.read_sql_query(
    """SELECT 
    Student_ID,
    Course_Name,
    DOB 
    FROM Student_Users
    """,
    connection
)  # View every student accounts as admin
stva2 = pd.read_sql_query(
    """SELECT
    [Date/Time]
    FROM Enrollment
    """,
    connection
)
stva3 = pd.read_sql_query(
    """SELECT
    Username,
    [Full Name],
    Email
    FROM Student_Username
    """,
    connection
)
stva4 = pd.read_sql_query(
    """SELECT
    Module1,
    Module2,
    Module3, 
    Module4, 
    OptionalModule1, 
    OptionalModule2, 
    OptionalModule3
    FROM Grades
    """,
    connection
)
view_students_admin = pd.concat([stva1, stva2, stva3, stva4], axis=1)
# Multiple databases merged into one
# to view every student detail as admin

tva1 = pd.read_sql_query(
    """SELECT
    Username,
    [Full Name],
    Email
    FROM Teacher_Username""",
    connection
)
tva2 = pd.read_sql_query(
    """SELECT
    Teacher_ID,
    Course,
    Title
    FROM Teacher_Users""",
    connection
)
view_teachers_admin = pd.concat([tva1, tva2], axis=1)
# Multiple databases merged into one
# to view every teacher detail as admin

def view_courses_details():
    ''' View all of the courses and their details (no arguments necessary) '''
    print(view_Courses.head(100000)) # display courses


def admin_view_student():
    ''' View the details of every teacher in the database as admin (no arguments necessary) '''
    print(view_students_admin.head(100000))      # display every student


def admin_view_teacher():
    ''' View the details of every teacher in the database as admin (no arguments necessary) '''
    print(view_teachers_admin.head(100000))  # display every teacher


class Sort:
    ''' Simply to group the "sort" commands. Sort the sorts '''
    def ascend_4():
        ''' Simply to group the "sort" commands. Sort the sorts '''
        print(sort4_ascending.head(100000))

    def descend_4():
        ''' Simply to group the "sort" commands. Sort the sorts '''
        print(sort4_descending.head(100000))

    def ascend_id_4():
        ''' Simply to group the "sort" commands. Sort the sorts '''
        print(sort4_ascending_id.head(100000))

    def descend_id_4():
        ''' Simply to group the "sort" commands. Sort the sorts '''
        print(sort4_descending_id.head(100000))

def main_menu():  # main menu command
    ''' The main part of the program this functions makes the whole program start and function  '''
    while True:
        print(
            "\nChoose action, press;", 
            "\n 1. To log in to a student account, ",
            "\n 2. To log in to a teacher, ",
            "\n 3. To log in as admin, ",
            "\n 4. To view courses, ",
            "\n 5. To view enrollment procedures, ",
            "\n 6. To exit:   "
        )  # Choose an action and procede
        choice = input("\nInput your choice: ")  # Input a choice between 1 and 6
        if choice == "1":  # Choice 1
            StudentAction.student_action()
        elif choice == "2":  # Choice 2
            TeacherAction.teacher_action()
        elif choice == "3":  # Choice 3
            while True:
                print("\nYou have chosen to log in to as admin")
                admin_exit = input(
                    "\nPress 'Enter' to procede or enter 'Return': "
                )  # Ensure the possiblity to go back if it was a missclick
                if admin_exit == "Return":
                    break
                if admin_exit == "":
                    admin_user = "CU"  # Username in code to ensure security
                    admin_login = input("\nEnter username: ")
                    if admin_login != admin_user:
                        print("\nInput Invalid")
                        continue
                    if admin_login == admin_user:
                        print("\nCorrect")
                        admin_pass = "M"
                        # Password in code to ensure security
                        admin_password = input("\nEnter admin password (1 attempt): ")
                        if admin_password != admin_pass:
                            print("\nPassword Incorrect")
                            break
                        print("\nLogin successful")
                    while True:
                        admin_action = input(
                            "\nChoose an action;"\
                            "\n 1. Manage student accounts, "\
                            "\n 2. Manage teacher accounts, "\
                            "\n 3. Manage courses, "\
                            "\n 4. To exit:     "
                        )  # Choose a admin action
                        if admin_action == "1":
                            while True:
                                admin_student = input(
                                    "\nYou have chosen to manage student accounts, "\
                                    "choose an action;"\
                                    "\n 1. View student accounts,"\
                                    "\n 2. Update a student account, "\
                                    "\n 3. Create a student account, "\
                                    "\n 4. Delete a student account, "\
                                    "\n 5. Exit:       "
                                )  # Choose a student management action
                                if admin_student == "1":
                                    admin_view_student()  # View every student account as admin
                                    continue
                                if admin_student == "2":
                                    Student.admin_update_student()  # check admin_commands.py
                                    continue
                                if admin_student == "3":
                                    Student.admin_create_student()  # check admin_commands.py
                                    continue
                                if admin_student == "4":
                                    Student.admin_delete_student()  # check admin_commands.py
                                    continue
                                if admin_student == "5":
                                    print("Exit successful")  # To exit
                                    break
                                print(
                                    "Input Invalid"
                                )  # To return to prompt if input not recognized
                                continue
                        elif admin_action == "2":
                            while True:
                                admin_teacher = input(
                                    "\nYou have chosen to manage teacher accounts,"\
                                    "choose an action;"\
                                    "\n 1. View teacher accounts, "\
                                    "\n 2. Update a teacher account, "\
                                    "\n 3. Create a teacher account, "\
                                    "\n 4. Delete a teacher account, "\
                                    "\n 5. Exit:       "
                                )  # Choose a teacher management action
                                if admin_teacher == "1":
                                    admin_view_teacher()  # View every teacher account as admin
                                    continue
                                if admin_teacher == "2":
                                    Teacher.admin_update_teacher()  # check admin_commands.py
                                    continue
                                if admin_teacher == "3":
                                    Teacher.admin_create_teacher()  # check admin_commands.py
                                    continue
                                if admin_teacher == "4":
                                    Teacher.admin_delete_teacher()  # check admin_commands.py
                                    continue
                                if admin_teacher == "5":
                                    print("\nExit successful")  # To exit
                                    break
                                # To return to prompt if input not recognized
                                print("\nInput Invalid")
                                continue
                        elif admin_action == "3":
                            course_admin = input(
                            "\nYou have chosen to manage courses, choose an action;"\
                            "\n 1. Create a course, "\
                            "\n 2. Update a course, "\
                            "\n 3. Delete a course, "\
                            "\n 4. To exit:      "
                            )  # Choose a course management action
                            if course_admin == "1":  # Create a new course
                                Course.admin_create_course() #check admin_commands_2.py
                                continue
                            if course_admin == "2":
                                Course.admin_update_course() #check admin_command_2.py
                            if course_admin == "3":
                                Course.admin_delete_course() #check admin_command_2.py
                            if course_admin == "4":  # To exit
                                print("\nExit successful")
                                break
                            # Return to prompt if input not recognised
                            input("\nInput Invalid")
                            continue
                        if admin_action == "4":  # To exit
                            print("\nExit successful")
                            break
                        if admin_action != ["1", "2", "3", "4"]:
                            print(
                            "\nInput Invalid"
                        )  # Return to prompt if input not recognised
                        continue
                else:
                    print("\nInput Invalid")  # Return to prompt if input not recognised
                    continue
        elif choice == "4":  # Choice 4
            view_courses_details()  # View every courses
            input(
                "\n Press 'Enter' to go back to main menu.  "
            )  # To prevent the 'continue' to execute right away
            continue
        elif choice == "5":  # Choice 5
            webbrowser.open(
                "https://shorturl.at/xBRV9"
            )  # Opens Coventry University Enrollment website
            input("\n Press 'Enter' to go back to main menu.  ")
            continue
        elif choice == "6":  # Choice 6
            print("\nApp exit successful")    # Exits program
            cursor.close()                    # Closes databese and connection
            connection.close()
            break
        print("\nInput Invalid")              # Return to prompt if input not recognised
        continue

main_menu()  # To start the program

input(
    "\nPress 'Enter' to close.  "
)  # To prevent the program from shutting down immediately
