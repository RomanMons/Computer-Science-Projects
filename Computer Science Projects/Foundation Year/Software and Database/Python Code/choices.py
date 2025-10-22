''' Imports SQLite3 so that I can use the database (school.db) in my program  '''
import sqlite3  # imported to be able to use sql queries
import pandas as pd  # imported to display databases, read sql queries
from isAny import (
    isUppercase,
    isLowercase,
    isSpace,
    isSymbol,
)  # explained in file

pd.options.display.max_columns = None  # To remove restraints on the number
pd.options.display.max_rows = None     # of rows and columns that 'pandas' displays

connection = sqlite3.connect(
    "school.db"
)  # To connect to the database conataining all the data
   # (Students, Teachers, Courses, Enrollment,  Attendance, Grades)
cursor = connection.cursor()  # Just to make it easier to type

class StudentAction:
    ''' Simply to seperate student actions from teacher actions '''
    def student_action():
        ''' Actions possible for a student account (no arguments necessary) '''
        while True:
            print(
                "\nYou have chosen to log in to a student account", 
                "\n(Enter 'Return' to return to main menu)"
            )  # Ensure the possiblity to go back if it was a missclick
            student_user = input("\nEnter username: ")  # Student username input
            cursor.execute(
                f"""SELECT Username
                FROM Student_Username 
                WHERE NOT EXISTS (SELECT * 
                FROM Student_Username 
                WHERE Username = '{student_user}');"""
            )  # Find User from Student_Users table
            if student_user == "Return":  # If 'Return' is inputted to program goes back
                break
            if cursor.fetchall():  # Check if the inputted user exists
                print("\nUser does not exist.")
                continue
            student_pass  = cursor.execute(
                f"""SELECT Password
                FROM Student_Username 
                WHERE username = '{student_user}'"""
                )
            student_fetch = student_pass.fetchone()
            student_word = student_fetch[0]
            if student_word == "pass":
                    # If the password = 'pass'
                    # which is the default password value a password has to be chosen
                while True:
                    paswrd = input(
                        "\nCreate a strong password, containing at least;"\
                        "\n 8 charcters,"\
                        "\n 1 Uppercase character,"\
                        "\n 1 Lowercase character,"\
                        "\n 1 Special charcter (?, !, %, &,...),"\
                        "\n 1 Digit: "
                    )
                    if isSpace(paswrd) is True:
                        print("\nPassword cannot contain any spaces")
                        continue
                    if (
                        len(paswrd) < 8
                        and isUppercase(paswrd) is False
                        or isLowercase(paswrd) is False
                        or isSymbol(paswrd) is False
                        or isSpace(paswrd) is True
                    ):
                        continue
                    if (
                        len(paswrd) >= 8
                        and isUppercase(paswrd) is True
                        and isLowercase(paswrd) is True
                        and isSymbol(paswrd) is True
                        and isSpace(paswrd) is False
                    ):
                        print("\nPassword created successfully")
                        cursor.execute(
                            f"""UPDATE Student_Username
                            SET Password = '{paswrd}'
                            WHERE Username = '{student_user}';"""
                        )  # Create a strong password and then
                        # updates the concerned student's password
                        connection.commit()
                        break
            else:
                c = 0
                while c < 3:
                    c += 1
                    pwd = input(
                        "\nEnter password (2 attempts): "
                    )  # Input user password with only 2 attempts allowed
                    # if more are made the program resets
                    cursor.execute(
                        f"""SELECT Username
                        FROM Student_Username 
                        WHERE EXISTS (SELECT '{student_user}'
                        FROM Student_Username
                        WHERE Password = '{pwd}');"""
                    )
                    if cursor.fetchall():
                        print("\nCorrect")
                    elif not cursor.fetchall():
                        print("\nPassword incorrect")
                        pwd2 = input("\n 1 attempt left: ")
                        cursor.execute(
                            f"""SELECT Username
                            FROM Student_Username
                            WHERE NOT EXISTS (SELECT '{student_user}'
                            FROM Student_Username 
                            WHERE Password = '{pwd2}');"""
                        )
                        if cursor.fetchall():
                            print("\nAccess Denied")
                            break
                        print("\nCorrect \nLogin successful")
                    print(
                        "\nChoose an action: ",
                        "\n 1. To view account details,", 
                        "\n 2. To manage account details,", 
                        "\n 3. To exit:   "
                    )  # Choose an student management action
                    student_choice = input("\nInput choice: ")
                    if student_choice == "3":
                        print("\nExit")
                        break
                    while True:
                        if (
                            student_choice == "1"
                        ):  # View personal student account details
                            print(
                                "\n You have chosen to view you account details:\n"
                            )
                            # Fetching Student ID to then use it
                            # as a primary key to get the info needed from
                            # the databases, for the dataframe
                            studentid = cursor.execute(
                                f"""SELECT [Student ID]
                                FROM Student_Username
                                WHERE Username
                                = '{student_user}';"""
                            )
                            s_id = studentid.fetchone()
                            sql_s_id = s_id[0]
                            stv1 = pd.read_sql_query(
                                f"""SELECT
                                Student_ID,
                                Course_Name
                                FROM Student_Users
                                WHERE Student_ID
                                = '{sql_s_id}';""",
                                connection
                            )
                            stv2 = pd.read_sql_query(
                                f"""SELECT
                                Username,
                                Password,
                                Email,
                                [Full Name]
                                FROM Student_Username
                                WHERE [Student ID]
                                = '{sql_s_id}';""",
                                connection
                            )
                            stv3 = pd.read_sql_query(
                                f"""SELECT
                                Enrolled
                                FROM Enrollment
                                WHERE [Student ID]
                                = '{sql_s_id}';""",
                                connection
                            )
                            stv4 = pd.read_sql_query(
                                f"""SELECT
                                Module1, 
                                Module2, 
                                Module3, 
                                Module4, 
                                OptionalModule1, 
                                OptionalModule2, 
                                OptionalModule3 
                                FROM Grades
                                WHERE [Student.ID]
                                = '{sql_s_id}';""",
                                connection
                            )
                            view_student_users = pd.concat([stv1, stv2, stv3, stv4], axis=1)
                            print(view_student_users.head(100000))
                            break
                        if student_choice == "2":
                            student_modify_command = input(
                                "\nYou have decided to modify your account details:"\
                                "\n Enter '1' to change password"\
                                "\n Enter '2' to exit:    "
                            )  # Modify account details (password) or exit
                            if student_modify_command == "2":  # Exit
                                print("\nExit successful")
                                break
                            if (
                                student_modify_command == "1"
                            ):  # Change password and make sure it's a strong one
                                while True:
                                    passwd = input(
                                        "\nCreate a strong password, containing at least;"\
                                        "\n 8 charcters, "\
                                        "\n 1 Uppercase character, "\
                                        "\n 1 Lowercase character, "\
                                        "\n 1 Special charcter (?, !, %, &,...), "\
                                        "\n 1 Digit: "
                                    )
                                    if isSpace(passwd) is True:
                                        print("\nPassword cannot contain any spaces")
                                        continue
                                    if (
                                        len(passwd) < 8
                                        and isUppercase(passwd) is False
                                        or isLowercase(passwd) is False
                                        or isSymbol(passwd) is False
                                        or isSpace(passwd) is True
                                    ):
                                        continue
                                    if (
                                        len(passwd) >= 8
                                        and isUppercase(passwd) is True
                                        and isLowercase(passwd) is True
                                        and isSymbol(passwd) is True
                                        and isSpace(passwd) is False
                                    ):
                                        print("\nPassword created successfully")
                                        cursor.execute(
                                            f"""UPDATE Student_Username
                                            SET Password = '{passwd}'
                                            WHERE Username = '{student_user}';"""
                                        )
                                        connection.commit()
                                        break

class TeacherAction:
    ''' Simply to seperate teacher actions from student actions '''
    def teacher_action():
        ''' Actions possible for a teacher account (no arguments necessary) '''
        while True:
            print(
            "\nYou have chosen to log in to a teacher account ",
            "\n(Enter 'Return' to return to main menu)"
            )  # Ensure the possiblity to go back if it was a missclick
            teacher_user = input("\nEnter username: ")  # Enter Teacher username
            cursor.execute(
                f"""SELECT Username
                FROM Teacher_Username
                WHERE NOT EXISTS (SELECT * 
                FROM Teacher_Username 
                WHERE Username = '{teacher_user}');"""
            )  # Check if the user exists
            if teacher_user == "Return":
                print("\nExit successful")
                break
            if cursor.fetchall():
                print("\nUser does not exist.")
                continue
            teacher_pass = cursor.execute(
                f"""SELECT Password
                FROM Teacher_Username
                WHERE Username = '{teacher_user}'"""
                )
            teacher_fetch = teacher_pass.fetchone()
            teacher_word = teacher_fetch[0]
            if teacher_word == "pass":
                # If the password = 'pass'
                # which is the default password value a password has to be chosen
                while True:
                    paswrdt = input(
                        "\nCreate a strong password, containing at least;"\
                        "\n 8 charcters, "\
                        "\n 1 Uppercase character, "\
                        "\n 1 Lowercase character, "\
                        "\n 1 Special charcter (?, !, %, &,...), "\
                        "\n 1 Digit: "
                                    )
                    if isSpace(paswrdt) is True:
                        print("\nPassword cannot contain any spaces")
                        continue
                    if (
                        len(paswrdt) < 8
                        and isUppercase(paswrdt) is False
                        or isLowercase(paswrdt) is False
                        or isSymbol(paswrdt) is False
                        or isSpace(paswrdt) is True
                    ):
                        continue
                    if (
                        len(paswrdt) >= 8
                        and isUppercase(paswrdt) is True
                        and isLowercase(paswrdt) is True
                        and isSymbol(paswrdt) is True
                        and isSpace(paswrdt) is False
                    ):
                        print("\nPassword created successfully")
                        cursor.execute(
                            f"""UPDATE Teacher_Username
                            SET Password = '{paswrdt}'
                            WHERE Username = '{teacher_user}';"""
                        )  # Create a strong password
                        #and then updates the concerned teacher's password
                        connection.commit()
                        break
            else:
                c = 0
                while c < 3:
                    c += 1
                    pwd = input("\nEnter password (2 attempts): ")
                    cursor.execute(
                        f"""SELECT Username
                        FROM Teacher_Username
                        WHERE EXISTS (SELECT '{teacher_user}'
                        FROM Teacher_Username
                        WHERE Password = '{pwd}');"""
                    )  # Password input with 2 attempts else access is denied
                    if cursor.fetchall():
                        print("\nCorrect")
                    elif not cursor.fetchall():
                        print("\nPassword incorrect")
                        pwd2 = input(" 1 attempt left: ")
                        cursor.execute(
                            f"""SELECT Username
                            FROM Teacher_Username
                            WHERE NOT EXISTS (SELECT '{teacher_user}'
                            FROM Teacher_Username
                            WHERE Password = '{pwd2}');"""
                        )
                        if cursor.fetchall():
                            print("\nAccess Denied")
                            break
                        print("\nCorrect \nLogin successful")
                    print(
                        "\nChoose an action:",
                        "\n 1. To view account details, ",
                        "\n 2. To manage account details, ",
                        "\n 3. To manage student details, ",
                        "\n 4. To exit:    "
                    )  # Choose an teacher action to execute
                    teacher_choice = input("\nInput choice: ")  # Input choice 1-4
                    if teacher_choice == "4":
                        print("\nExit")
                        break
                    if (
                        teacher_choice == "1"
                        or teacher_choice == "2"
                        or teacher_choice == "3"
                    ):
                        while True:
                            if teacher_choice == "1":
                                # Fetching Teacher ID to then use it
                                # as a primary key to get the info needed from
                                # the databases, for the dataframe
                                teacherid = cursor.execute(
                                    f"""SELECT [Teacher ID]
                                    FROM Teacher_Username
                                    WHERE Username
                                    = '{teacher_user}';"""
                                )
                                t_id = teacherid.fetchone()
                                sql_t_id = t_id[0]
                                tv1 = pd.read_sql_query(
                                    f"""SELECT
                                    Teacher_ID,
                                    Course
                                    Title
                                    FROM Teacher_Users
                                    WHERE Teacher_ID
                                    = '{sql_t_id}';""",
                                    connection
                                )
                                tv2 = pd.read_sql_query(
                                    f"""SELECT
                                    Username,
                                    Password,
                                    Email,
                                    [Full Name]
                                    FROM Teacher_Username
                                    WHERE [Teacher ID]
                                    = '{sql_t_id}';""",
                                    connection
                                )
                                view_teachers_admin = pd.concat([tv1, tv2], axis=1)
                                print(view_teachers_admin.head(100000))
                                break
                            if teacher_choice == "2":
                                teacher_modify_command = input(
                                    "\nYou have decided to modify your account details:"\
                                    "\n Enter '1' to change password, "\
                                    "\n Enter '2' to exit:    "
                                )  # Manage account details (password) or exit
                                if teacher_modify_command == "2":  # Exit
                                    print("\nExit successful")
                                    break
                                if teacher_modify_command == "1":  # Change password
                                    while True:
                                        pswrd = input(
                                            "\nCreate a strong password, containing at least;"\
                                            "\n 8 charcters, "\
                                            "\n 1 Uppercase character, "\
                                            "\n 1 Lowercase character, "\
                                            "\n 1 Special charcter (?, !, %, &,...), "\
                                            "\n 1 Digit: "
                                        )
                                        if isSpace(pswrd) is True:
                                            print("\nPassword cannot contain any spaces")
                                            continue
                                        if (
                                            len(pswrd) < 8
                                            and isUppercase(pswrd) is False
                                            or isLowercase(pswrd) is False
                                            or isSymbol(pswrd) is False
                                            or isSpace(pswrd) is True
                                        ):
                                            continue
                                        if (
                                            len(pswrd) >= 8
                                            and isUppercase(pswrd) is True
                                            and isLowercase(pswrd) is True
                                            and isSymbol(pswrd) is True
                                            and isSpace(pswrd) is False
                                        ):
                                            print("\nPassword created successfully")
                                            cursor.execute(
                                                f"""UPDATE Teacher_Username
                                                SET Password = '{pswrd}'
                                                WHERE Username = '{teacher_user}';"""
                                            )
                                            connection.commit()
                                            break
                            if teacher_choice == "3":
                                teacher_student_command = input(
                                    "\nYou have chosen to manage a student account; "\
                                    "\n Enter the STUDENT ID of the student's account to manage: "\
                                    "\n (Student must be from the same course as the teacher)"\
                                    "\n (Enter 'Exit' to exit)       "
                                )  # Manage student account
                                teacherid = cursor.execute(
                                    f"""SELECT [Teacher ID]
                                    FROM Teacher_Username
                                    WHERE Username
                                    = '{teacher_user}';"""
                                )
                                t_id = teacherid.fetchone()
                                sql_t_id = t_id[0]
                                course_db = cursor.execute(
                                    f"""SELECT Course
                                    FROM Teacher_Users
                                    WHERE Teacher_ID
                                    = '{sql_t_id}'
                                    ;"""
                                )
                                course_fetch = course_db.fetchone()
                                course_sql = course_fetch[0]
                                cursor.execute(
                                    f"""SELECT Student_ID
                                    FROM Student_Users 
                                    WHERE EXISTS (SELECT User 
                                    FROM Student_Users
                                    WHERE Student_ID 
                                    = '{teacher_student_command}'
                                    AND Course_Name
                                    = '{course_sql}'
                                    );"""
                                )
                                if cursor.fetchall():
                                    print("Student found;")
                                    while True:
                                        teacher_action = input(
                                            "\nChoose an action, press;"\
                                            "\n 1. To add/modify grades, "\
                                            "\n 2. To update attendance, "\
                                            "\n 3. View account"
                                            "\n 4. To exit: "
                                        )  # To modify grades, attendance or exit
                                        if teacher_action == "1":
                                            while True:
                                                print(
                                                    "\nChoose a Module: ",
                                                    "\n 1. Module 1, ",
                                                    "\n 2. Module 2, ",
                                                    "\n 3. Module 3, ",
                                                    "\n 4. Module 4, ",
                                                    "\n 5. Optional Module 1, ",
                                                    "\n 6. Optional Module 2, ",
                                                    "\n 7. Optional Module 3, ",
                                                    "\n 8. To exit:   "
                                                )  # To choose the specific module to update
                                                module_choice = input("\n Enter option: ")
                                                if module_choice == "1":
                                                    student_grades = float(
                                                        input("\nEnter grades (0-100%): ")
                                                    )
                                                    if (
                                                        0.0 <= student_grades <= 100.0
                                                    ):
                                                        cursor.execute(
                                                            f"""UPDATE Grades
                                                            SET Module1 = '{student_grades}'
                                                            WHERE [Student.ID] 
                                                            = '{teacher_student_command}'"""
                                                        )
                                                        connection.commit()
                                                        print("\nGrade added successfully")
                                                        break
                                                    print("\nInput Invalid")
                                                    continue
                                                if module_choice == "2":
                                                    student_grades = float(
                                                        input("\nEnter grades (0-100%): ")
                                                    )
                                                    if (
                                                        0.0 <= student_grades <= 100.0
                                                    ):
                                                        cursor.execute(
                                                            f"""UPDATE Grades
                                                            SET Module2 = '{student_grades}'
                                                            WHERE [Student.ID] 
                                                            = '{teacher_student_command}'"""
                                                        )
                                                        connection.commit()
                                                        print("\nGrade added successfully")
                                                        break
                                                    print("\nInput Invalid")
                                                    continue
                                                if module_choice == "3":
                                                    student_grades = float(
                                                        input("\nEnter grades (0-100%): ")
                                                    )
                                                    if (
                                                        0.0 <= student_grades <= 100.0
                                                    ):
                                                        cursor.execute(
                                                            f"""UPDATE Grades
                                                            SET Module3 = '{student_grades}'
                                                            WHERE [Student.ID] 
                                                            = '{teacher_student_command}'"""
                                                        )
                                                        connection.commit()
                                                        print("\nGrade added successfully")
                                                        break
                                                    print("\nInput Invalid")
                                                    continue
                                                if module_choice == "4":
                                                    student_grades = float(
                                                        input("\nEnter grades (0-100%): ")
                                                    )
                                                    if (
                                                        0.0 <= student_grades <= 100.0
                                                    ):
                                                        cursor.execute(
                                                            f"""UPDATE Grades
                                                            SET Module4 = '{student_grades}'
                                                            WHERE [Student.ID] 
                                                            = '{teacher_student_command}'"""
                                                        )
                                                        connection.commit()
                                                        print("\nGrade added successfully")
                                                        break
                                                    print("\nInput Invalid")
                                                    continue
                                                if module_choice == "5":
                                                    student_grades = float(
                                                        input("\nEnter grades (0-100%): ")
                                                    )
                                                    if (
                                                        0.0 <= student_grades <= 100.0
                                                    ):
                                                        cursor.execute(
                                                            f"""UPDATE Grades
                                                            SET OptionalModule1 = '{student_grades}'
                                                            WHERE [Student.ID] 
                                                            = '{teacher_student_command}'"""
                                                        )
                                                        connection.commit()
                                                        print("\nGrade added successfully")
                                                        break
                                                    print("\nInput Invalid")
                                                    continue
                                                if module_choice == "6":
                                                    student_grades = float(
                                                        input("\nEnter grades (0-100%): ")
                                                    )
                                                    if (
                                                        0.0 <= student_grades <= 100.0
                                                    ):
                                                        cursor.execute(
                                                            f"""UPDATE Grades
                                                            SET OptionalModule2 = '{student_grades}'
                                                            WHERE [Student.ID] 
                                                            = '{teacher_student_command}'"""
                                                        )
                                                        connection.commit()
                                                        print("\nGrade added successfully")
                                                        break
                                                    print("\nInput Invalid")
                                                    continue
                                                if module_choice == "7":
                                                    student_grades = float(
                                                        input("\nEnter grades (0-100%): ")
                                                    )
                                                    if (
                                                        0.0 <= student_grades <= 100.0
                                                    ):
                                                        cursor.execute(
                                                            f"""UPDATE Grades
                                                            SET OptionalModule3 = '{student_grades}'
                                                            WHERE [Student.ID] 
                                                            = '{teacher_student_command}'"""
                                                        )
                                                        connection.commit()
                                                        print("\nGrade added successfully")
                                                        break
                                                    print("\nInput Invalid")
                                                    continue
                                                if module_choice == "8":
                                                    print("\nExit successful")
                                                    break
                                                print("\nInput Invalid")
                                                continue
                                        elif teacher_action == "2":
                                            while True:
                                                print(
                                                    "\nChoose a Module:", 
                                                    "\n 1. Module 1",
                                                    "\n 2. Module 2, ",
                                                    "\n 3. Module 3, ",
                                                    "\n 4. Module 4, ",
                                                    "\n 5. Optional Module 1, ",
                                                    "\n 6. Optional Module 2, ",
                                                    "\n 7. Optional Module 3, ",
                                                    "\n 8. To exit:   "
                                                )  # To choose the specific module to update or exit
                                                module_attendance = input(
                                                    "\n Enter option: "
                                                )
                                                if module_attendance == "1":
                                                    student_attendance = int(
                                                        input(
                                                            "\nEnter attendance percentage: "
                                                        )
                                                    )
                                                    if (
                                                        0 <= student_attendance <= 100
                                                    ):
                                                        cursor.execute(
                                                            f"""UPDATE Attendance
                                                            SET Module1 = {student_attendance}
                                                            WHERE StudentID
                                                            = '{teacher_student_command}'"""
                                                        )
                                                        connection.commit()
                                                        print("\nAttendance updated successfully")
                                                        break
                                                    print("\nInput Invalid")
                                                    continue
                                                if module_attendance == "2":
                                                    student_attendance = int(
                                                        input(
                                                            "\nEnter attendance percentage: "
                                                        )
                                                    )
                                                    if (
                                                        0 <= student_attendance <= 100
                                                    ):
                                                        cursor.execute(
                                                            f"""UPDATE Attendance
                                                            SET Module2 = {student_attendance}
                                                            WHERE StudentID 
                                                            = '{teacher_student_command}'"""
                                                        )
                                                        connection.commit()
                                                        print("\nAttendance updated successfully")
                                                        break
                                                    print("\nInput Invalid")
                                                    continue
                                                if module_attendance == "3":
                                                    student_attendance = int(
                                                        input(
                                                            "\nEnter attendance percentage: "
                                                        )
                                                    )
                                                    if (
                                                        0 <= student_attendance <= 100
                                                    ):
                                                        cursor.execute(
                                                            f"""UPDATE Attendance
                                                            SET Module3 = {student_attendance}
                                                            WHERE StudentID 
                                                            = '{teacher_student_command}'"""
                                                        )
                                                        connection.commit()
                                                        print("\nAttendance updated successfully")
                                                        break
                                                    print("\nInput Invalid")
                                                    continue
                                                if module_attendance == "4":
                                                    student_attendance = int(
                                                        input(
                                                            "\nEnter attendance percentage: "
                                                        )
                                                    )
                                                    if (
                                                        0 <= student_attendance <= 100
                                                    ):
                                                        cursor.execute(
                                                            f"""UPDATE Attendance
                                                            SET Module4 = {student_attendance}
                                                            WHERE StudentID 
                                                            = '{teacher_student_command}'"""
                                                        )
                                                        connection.commit()
                                                        print("\nAttendance updated successfully")
                                                        break
                                                    print("\nInput Invalid")
                                                    continue
                                                if module_attendance == "5":
                                                    student_attendance = int(
                                                        input(
                                                            "\nEnter attendance percentage: "
                                                        )
                                                    )
                                                    if (
                                                        0 <= student_attendance <= 100
                                                    ):
                                                        cursor.execute(
                                                            f"""UPDATE Attendance
                                                            SET OptionalModule1 
                                                            = {student_attendance}
                                                            WHERE StudentID 
                                                            = '{teacher_student_command}'"""
                                                        )
                                                        connection.commit()
                                                        print("\nAttendance updated successfully")
                                                        break
                                                    print("\nInput Invalid")
                                                    continue
                                                if module_attendance == "6":
                                                    student_attendance = int(
                                                        input(
                                                            "\nEnter attendance percentage: "
                                                        )
                                                    )
                                                    if (
                                                        0 <= student_attendance <= 100
                                                    ):
                                                        cursor.execute(
                                                            f"""UPDATE Attendance
                                                            SET OptionalModule2 
                                                            = {student_attendance}
                                                            WHERE StudentID 
                                                            = '{teacher_student_command}'"""
                                                        )
                                                        connection.commit()
                                                        print("\nAttendance updated successfully")
                                                        break
                                                    print("\nInput Invalid")
                                                    continue
                                                if module_attendance == "7":
                                                    student_attendance = int(
                                                        input(
                                                            "\nEnter attendance percentage: "
                                                        )
                                                    )
                                                    if (
                                                        0 <= student_attendance <= 100
                                                    ):
                                                        cursor.execute(
                                                            f"""UPDATE Attendance
                                                            SET OptionalModule3 
                                                            = {student_attendance}
                                                            WHERE StudentID 
                                                            = '{teacher_student_command}'"""
                                                        )
                                                        connection.commit()
                                                        print("\nAttendance updated successfully")
                                                        break
                                                    print("\nInput Invalid")
                                                    continue
                                                if module_choice == "8":
                                                    print("\nExit successful")
                                                    break
                                                print("\nInput Invalid")
                                                continue
                                        elif teacher_action == "3":
                                            tvs1 = pd.read_sql_query(
                                                f"""SELECT
                                                First_Name,
                                                Last_Name,
                                                Course_Name
                                                FROM Student_User
                                                WHERE Student_ID
                                                = '{teacher_student_command}'
                                                """,
                                                connection
                                            )
                                            tvs2 = pd.read_sql_query(
                                                f"""SELECT
                                                Username,
                                                Email
                                                FROM Student_Username
                                                WHERE [Student ID]
                                                = '{teacher_student_command}'
                                                """,
                                                connection
                                            )
                                            teacher_view_student = pd.concat([tvs1, tvs2], axis=1)
                                            print(teacher_view_student.head(100000))
                                            while True:
                                                xtra_info = input("\n Extra information"\
                                                    "\n 1. Attendance"\
                                                    "\n 2. Grades"\
                                                    "\n 3. Exit"
                                                    )
                                                if xtra_info == "1":
                                                    tvsa = pd.read_sql_query(
                                                        f"""SELECT
                                                        Module1, 
                                                        Module2, 
                                                        Module3, 
                                                        Module4, 
                                                        OptionalModule1, 
                                                        OptionalModule2, 
                                                        OptionalModule3
                                                        FROM Attendance
                                                        WHERE StudentID
                                                        = '{teacher_student_command}'
                                                        """,
                                                        connection
                                                    )
                                                    tvs_attendance = pd.concat(
                                                        [tvs1, tvs2, tvsa],
                                                        axis=1
                                                        )
                                                    print(tvs_attendance)
                                                    continue
                                                if xtra_info == "2":
                                                    tvsg = pd.read_sql_query(
                                                        f"""SELECT
                                                        Module1, 
                                                        Module2, 
                                                        Module3, 
                                                        Module4, 
                                                        OptionalModule1, 
                                                        OptionalModule2, 
                                                        OptionalModule3
                                                        FROM Grades
                                                        WHERE [Student.ID]
                                                        = '{teacher_student_command}'
                                                        """,
                                                        connection
                                                    )
                                                    tvs_grades = pd.concat(
                                                        [tvs1, tvs2, tvsg],
                                                        axis=1
                                                        )
                                                    print(tvs_grades)
                                                    continue
                                                if xtra_info == "3":
                                                    print("\nExit successful")
                                                    break
                                                print("\nInput Invalid")
                                                continue
                                        elif teacher_action == "4":
                                            print("\nExit successful")
                                            break
                                        print("\nInput Invalid")
                                        continue
                                elif teacher_student_command == "Exit":
                                    print("\nExit successful")
                                    break
                                print("\nStudent not found")
                                continue
