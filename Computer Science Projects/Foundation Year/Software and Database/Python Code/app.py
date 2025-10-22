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
   #(Students, Teachers, Courses, Enrolment,  Attendance, Grades)
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
    FROM Enrolment
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


def search_courses(): # Search for a course
    ''' Search for a specific course in the Courses table (no arguments necessary) '''
    while True:
        course_name = input("\n\nSearch for course name: "
                            "\n (Enter 'Exit' to exit):       "
                            )
        cdf = view_Courses[view_Courses.Name == course_name]
        if course_name == "Exit":
            print("Exit successful")
            break
        while True:
            if cdf.empty:
                print("Course not found")
                break
            print(cdf)
            break

def view_courses_details(): # Display course details
    ''' View course details, and the possibility to sort
    or search for a specific sort (no arguments necessary) '''
    while True:
        vc = view_Courses
        if vc.empty:
            print("There are no courses available")
            break
        asc_c = vc.sort_values(by=['Name']) # a to z
        desc_c = vc.sort_values(by=['Name'], ascending=False) # z to a
        course_action = input("You have chosen to view courses, choose an action;"\
                        "\n 1. View courses"\
                        "\n 2. Sort courses"\
                        "\n 3. Search for a specific course"\
                        "\n 4. Exit:    "
                        )
        if course_action == "1":
            print(vc)
            continue
        if course_action == "2":
            while True:
                sort = input("Press;"\
                            "\n 1. To sort alphabetically,"\
                            "\n 2. To sort unalphabetically,"\
                            "\n 3. To exit:        "
                            )
                if sort == "1":
                    print(asc_c)
                    continue
                if sort == "2":
                    print(desc_c)
                    continue
                if sort == "3":
                    print("Exit successful")
                    break
                print("Input Invalid")
                continue
        if course_action == "3":
            search_courses()
            continue
        if course_action == "4":
            print("Exit successful")
            break
        print("Input Invalid")
        continue


def search_student_accounts(): # Search for a student account
    ''' Search for a specific student account 
    in the Student_Username table (no arguments necessary) '''
    while True:
        student_name = input("\n\nSearch for student's full name: "
                            "\n (Enter 'Exit' to exit):       "
                            )
        sdf = view_students_admin.loc[view_students_admin['Full Name'] == student_name]
        if student_name == "Exit":
            print("Exit successful")
            break
        while True:
            if sdf.empty:
                print("Student account not found")
                break
            print(sdf)
            break

def admin_view_student(): # View every student account as admin
    ''' View the details of every student as an admin, and the possibility to sort
    or search for a specific sort (no arguments necessary) '''
    while True:
        sc = view_students_admin
        if sc.empty:
            print("There are no student accounts")
            break
        asc_s = sc.sort_values(by=['Full Name']) # a to z
        desc_s = sc.sort_values(by=['Full Name'], ascending=False) # z to a
        sc_action = input("You have chosen to view student accounts, choose an action;"\
                        "\n 1. View accounts"\
                        "\n 2. Sort accounts"\
                        "\n 3. Search for a specific account"\
                        "\n 4. Exit:    "
                        )
        if sc_action == "1":
            print(sc)
            continue
        if sc_action == "2":
            while True:
                sc_sort = input("Press;"\
                            "\n 1. To sort alphabetically,"\
                            "\n 2. To sort unalphabetically,"\
                            "\n 3. To exit:        "
                            )
                if sc_sort == "1":
                    print(asc_s)
                    continue
                if sc_sort == "2":
                    print(desc_s)
                    continue
                if sc_sort == "3":
                    print("Exit successful")
                    break
                print("Input Invalid")
                continue
        if sc_action == "3":
            search_student_accounts()
            continue
        if sc_action == "4":
            print("Exit successful")
            break
        print("Input Invalid")
        continue


def search_teacher_accounts(): # Search for a teacher account
    ''' Search for a specific teacher account 
    in the Teacher_Username table (no arguments necessary) '''
    while True:
        teacher_name = input("\n\nSearch for student's full name: "
                            "\n (Enter 'Exit' to exit):       "
                            )
        tdf = view_teachers_admin.loc[view_teachers_admin['Full Name'] == teacher_name]
        if teacher_name == "Exit":
            print("Exit successful")
            break
        while True:
            if tdf.empty:
                print("Teacher account not found")
                break
            print(tdf)
            break

def admin_view_teacher(): # View every student account as admin
    ''' View the details of every teacher as an admin, and the possibility to sort
    or search for a specific sort (no arguments necessary) '''
    while True:
        tc = view_teachers_admin
        if tc.empty:
            print("There are no teacher accounts")
            break
        asc_t = tc.sort_values(by=['Full Name']) # a to z
        desc_t = tc.sort_values(by=['Full Name'], ascending=False) # z to a
        tc_action = input("You have chosen to view teacher accounts, choose an action;"\
                        "\n 1. View accounts"\
                        "\n 2. Sort accounts"\
                        "\n 3. Search for a specific account"\
                        "\n 4. Exit:    "
                        )
        if tc_action == "1":
            print(tc)
            continue
        if tc_action == "2":
            while True:
                tc_sort = input("Press;"\
                            "\n 1. To sort alphabetically,"\
                            "\n 2. To sort unalphabetically,"\
                            "\n 3. To exit:        "
                            )
                if tc_sort == "1":
                    print(asc_t)
                    continue
                if tc_sort == "2":
                    print(desc_t)
                    continue
                if tc_sort == "3":
                    print("Exit successful")
                    break
                print("Input Invalid")
                continue
        if tc_action == "3":
            search_teacher_accounts()
            continue
        if tc_action == "4":
            print("Exit successful")
            break
        print("Input Invalid")
        continue


def main_menu():  # main menu command
    ''' The main part of the program this functions makes the whole program start and function  '''
    while True:
        print(
            "\nChoose action, press;", 
            "\n 1. To log in to a student account, ",
            "\n 2. To log in to a teacher, ",
            "\n 3. To log in as admin, ",
            "\n 4. To view courses, ",
            "\n 5. To view Enrolment procedures, ",
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
                    admin_user = "CU_Admin"  # Username in code to ensure security
                    admin_login = input("\nEnter username: ")
                    if admin_login != admin_user:
                        print("\nInput Invalid")
                        continue
                    if admin_login == admin_user:
                        print("\nCorrect")
                        admin_pass = "GloryManchesterUnited!"
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
            )  # Opens Coventry University Enrolment website
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
