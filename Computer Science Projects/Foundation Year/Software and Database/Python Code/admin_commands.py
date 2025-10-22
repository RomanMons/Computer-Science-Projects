''' Imports SQLite3 so that I can use the database (school.db) in my program  '''
import sqlite3

# imported to be able to use sql queries
from datetime import datetime, date

# imported to be able to return a date and time for DOB and enrolment
import random

# imported for username creation to be able to make a random assortment of
# numbers
from isAny import isUppercase, isNumeric, isspace_and_alpha

# explained in file

connection = sqlite3.connect("school.db")
# To avoid a "database is locked" error
cursor = connection.cursor()


class Student:
    ''' Groups every student related functions executed by admin '''
    def admin_create_student():  # Create a new student account
        ''' Creates a new student account as admin (no arguments necessary) '''
        while True:
            input_create_sure = input(
                "\nPress 'Enter' to procede, enter 'Return' to exit: "
            )
            if input_create_sure == "Return":
                break
            if input_create_sure == "":
                    # Create username with first name, last name and then a
                    # randomized assortment of 4 numbers
                while True:
                    input_first_name = input(
                        "\nPlease enter 'First Name'(lowercase only): "
                    )
                    if (
                        isNumeric(input_first_name)
                        or not isspace_and_alpha(input_first_name)
                        or isUppercase(input_first_name)
                    ):
                        print(
                            "\nInput invalid (Use letters in lowercase only)"
                        )
                        continue
                    if not len(input_first_name) > 1:
                        print("\nInput Invalid")
                        continue
                    input_last_name = input(
                        "\nPlease enter 'Last Name'(lowercase only): "
                    )
                    if (
                        isNumeric(input_last_name)
                        or not isspace_and_alpha(input_last_name)
                        or isUppercase(input_last_name)
                        ):
                        print(
                            "\nInput invalid (Use letters in lowercase only)"
                        )
                        continue
                    if not len(input_last_name) > 1:
                        print("\nInput Invalid")
                        continue
                    break
                while True:
                    try:
                        day = int(input("\nPlease enter date \nEnter day: "))
                        month = int(input("Enter month: "))
                        year = int(input("Enter year: "))
                        user_dob = date(year, month, day)
                        print(user_dob)
                        break
                    except ValueError:
                        print("\nInvalid input in date")
                        continue
                while True:
                    first_letters = input_last_name[0:5]
                    last_letters = input_first_name[0:4]
                    number1 = random.randint(0, 9)
                    first_number = str(number1)
                    number2 = random.randint(0, 9)
                    second_number = str(number2)
                    number3 = random.randint(0, 9)
                    third_number = str(number3)
                    number4 = random.randint(0, 9)
                    last_number = str(number4)
                    new_user = (
                        first_letters
                        + last_letters
                        + first_number
                        + second_number
                        + third_number
                        + last_number
                    )
                    cursor.execute(
                        f"""SELECT Username
                        FROM Student_Username 
                        WHERE EXISTS (SELECT * 
                        FROM Student_Username 
                        WHERE Username 
                        = '{new_user}');"""
                    )
                    connection.commit()
                    # Redo number assortment if username already exists
                    if cursor.fetchall():
                        continue
                    else:
                        new_first_name = input_first_name.title()
                        new_last_name = input_last_name.title()
                        full_name = new_first_name + " " + new_last_name
                        email_user = new_user.replace(" ", "_")
                        # add '@coventry.ac.uk' to username to make student email
                        new_email = email_user + "@coventry.ac.uk"
                        input_student_course = input("\nEnter COURSE ID: ")
                        cursor.execute(
                            f"""SELECT [Course ID]
                            FROM Courses
                            WHERE EXISTS (SELECT *
                            FROM Courses
                            WHERE [Course ID] 
                            = '{input_student_course}');"""
                            )
                        if not cursor.fetchall():
                            print("\nCourse doesn't exist")
                            continue
                        else:
                            course_name = cursor.execute(
                                f"""SELECT Name
                                FROM Courses 
                                WHERE [Course ID]
                                ='{input_student_course}';"""
                            )
                            student_course = course_name.fetchone()
                            sql_student_course = student_course[0]
                            cursor.execute(
                                f"""INSERT INTO Student_Users
                                (First_Name,
                                Last_Name,
                                Course_Name, 
                                DOB,
                                User) 
                                VALUES 
                                ('{new_first_name}',
                                '{new_last_name}',
                                '{sql_student_course}',
                                '{user_dob}',
                                '{new_user}'
                                );"""
                            )  # add all the data to Student_Users and Student_Username databases
                            connection.commit()
                            student_id = cursor.execute(
                                f"""SELECT Student_ID
                                FROM Student_Users
                                WHERE User 
                                = '{new_user}';"""
                                )
                            values_student_id = student_id.fetchone()
                            sql_values_st_id = values_student_id[0]
                            # create an attendance, grade and enrolment row for
                            # newly added student
                            cursor.execute(
                                f"""INSERT INTO Student_Username
                                ([Full Name],
                                [Username],
                                Email,
                                [Student ID])
                                VALUES
                                ('{full_name}',
                                '{new_user}',
                                '{new_email}',
                                '{sql_values_st_id}'
                                );"""
                            )
                            connection.commit()
                            cursor.execute(
                                f"""INSERT INTO Attendance
                                (StudentID)
                                VALUES
                                ('{sql_values_st_id}');"""
                            )
                            connection.commit()
                            cursor.execute(
                                f"""INSERT INTO Grades
                                ('Student.ID')
                                VALUES
                                ('{sql_values_st_id}');"""
                            )
                            connection.commit()
                            cursor.execute(
                                f"""INSERT INTO Enrolment
                                ('Student ID')
                                VALUES
                                ('{sql_values_st_id}');"""
                            )
                            connection.commit()
                            print("\nStudent added successfully")
                        break

    def admin_delete_student():
        ''' Deletes an existing student account as admin (no arguments necessary) '''
        while True:
            # Delete a student with the possibility to go back if it was a
            # missclick
            student_id_delete = input(
                "\nInput the Student ID of the student account to delete (Enter 'Return' to exit): "
            )
            if student_id_delete == "Return":
                print("\nExit successful")
                break
            while True:
                print(student_id_delete)
                # To be sure it's the right student
                student_deletion_sure = input(
                    "\nAre you sure you want to delete this account ? "\
                    "(Enter 'yes' to continue, 'no' to go back): "
                )
                if student_deletion_sure == "no":
                    break
                if student_deletion_sure == "yes":
                    cursor.execute(
                        f"""SELECT Student_ID
                        FROM Student_Users 
                        WHERE EXISTS (SELECT Student_ID
                        FROM Student_Users 
                        WHERE Student_ID 
                        = '{student_id_delete}');"""
                    )  # Delete student account and everything linked to it
                    if cursor.fetchall():
                        cursor.execute(
                            f"""DELETE
                            FROM Student_Users 
                            WHERE Student_ID
                            = '{student_id_delete}'"""
                        )
                        connection.commit()
                        cursor.execute(
                            f"""DELETE
                            FROM Student_Username
                            WHERE [Student ID]
                            = '{student_id_delete}'"""
                        )
                        connection.commit()
                        cursor.execute(
                            f"""DELETE
                            FROM Attendance 
                            WHERE StudentID 
                            = '{student_id_delete}'"""
                        )
                        connection.commit()
                        cursor.execute(
                            f"""DELETE
                            FROM Grades 
                            WHERE [Student.ID] 
                            = '{student_id_delete}'"""
                        )
                        connection.commit()
                        cursor.execute(
                            f"""DELETE
                            FROM Enrolment
                            WHERE [Student ID] 
                            = '{student_id_delete}'"""
                        )
                        connection.commit()
                        print("\nDeletion Successful")
                        break
                        # Return to previous prompt if user not found
                    print("\nStudent account not found")
                    break
                # Return to previous prompt if input not recognised
                print("\nInput Invalid")
                continue

    def admin_update_student():
        ''' Updates an existing student account as admin (no arguments necessary) '''
        while True:
            # Update a student account and give the choice to procede or go
            # back
            input_student_id_update = input(
                "You have chosen to update a student account, "\
                "enter the STUDENT ID of the student account you wish to update: "\
                "\n(Enter 'Return' to exit)        "
            )
            if input_student_id_update == "Return":
                print("\nExit successful")
                break
            while True:
                print(input_student_id_update)
                # To be sure it's the right student
                student_deletion_sure = input(
                    "\nAre you sure you want to update this account ? "\
                    "(Enter 'yes' to continue, 'no' to go back): "
                )
                if student_deletion_sure == "no":
                    break
                if student_deletion_sure == "yes":
                    cursor.execute(
                        f"""SELECT Student_ID
                        FROM Student_Users 
                        WHERE EXISTS (SELECT Student_ID 
                        FROM Student_Users 
                        WHERE Student_ID 
                        = '{input_student_id_update}')"""
                    )  # Checks if user exists
                    if not cursor.fetchall():
                        print("\nStudent not found")
                        break
                    update_student_action = input(
                        "\nWhat do you wish to update: "\
                        "\n 1. Full name, "\
                        "\n 2. Enrolment, "\
                        "\n 3. Course: "
                    )
                    if update_student_action == "1":
                        while True:
                            # Change full name and thus student emaila
                            # and username
                            input_first_name_update = input(
                                "\nPlease enter 'First Name'(lowercase only): "
                            )
                            if (
                                isNumeric(input_first_name_update)
                                or not isspace_and_alpha(
                                    input_first_name_update
                                )
                                or isUppercase(input_first_name_update)
                            ):
                                print(
                                    "\nInput invalid ",
                                    "(Use letters in lowercase only)"
                                )
                                continue
                            if not len(input_first_name_update) > 1:
                                print("\nInput Invalid")
                                continue
                            input_last_name_update = input(
                                "\nPlease enter 'Last Name'(lowercase only): "
                            )
                            if (
                                isNumeric(input_last_name_update)
                                or not isspace_and_alpha(
                                    input_last_name_update
                                )
                                or isUppercase(input_last_name_update)
                            ):
                                print(
                                    "\nInput invalid ",
                                    "(Use letters in lowercase only)"
                                )
                                continue
                            if not (
                                len(input_last_name_update) > 1
                                    ):
                                print("\nInput Invalid")
                                continue
                            first_letters_update = (
                                input_last_name_update[0:5]
                                                    )
                            last_letters_update = input_first_name_update[0:4]
                            while True:
                                number1_update = random.randint(
                                    0, 9
                                )
                                first_number_update = str(
                                    number1_update
                                )
                                number2_update = random.randint(
                                    0, 9
                                )
                                second_number_update = str(
                                    number2_update
                                )
                                number3_update = random.randint(
                                    0, 9
                                )
                                third_number_update = str(
                                    number3_update
                                )
                                number4_update = random.randint(
                                    0, 9
                                )
                                last_number_update = str(
                                    number4_update
                                )
                                new_user_update = (
                                    first_letters_update
                                    + last_letters_update
                                    + first_number_update
                                    + second_number_update
                                    + third_number_update
                                    + last_number_update
                                )
                                # Redo number
                                # assortment if
                                # username already
                                # exists
                                cursor.execute(
                                    f"""SELECT Username
                                    FROM Student_Username 
                                    WHERE EXISTS (SELECT * 
                                    FROM Student_Username 
                                    WHERE Username = '{new_user_update}')"""
                                )
                                if cursor.fetchall():
                                    continue
                                new_first_name_update = (
                                input_first_name_update.title()
                                )
                                new_last_name_update = (
                                input_last_name_update.title()
                                )
                                no_sp_user_update = (
                                new_user_update.replace(
                                    " ", "_"
                                )
                                )
                                new_email_update = (
                                no_sp_user_update
                                + "@coventry.ac.uk"
                                )
                                cursor.execute(
                                    f"""UPDATE Student_Users
                                    SET First_Name
                                    = '{new_first_name_update}',
                                    Last_Name
                                    = '{new_last_name_update}',
                                    WHERE Student_ID 
                                    = '{input_student_id_update}';"""
                                )
                                connection.commit()
                                cursor.execute(
                                    f"""UPDATE Student_Username
                                    SET Username
                                    = '{no_sp_user_update}',
                                    Email
                                    = '{new_email_update}',
                                    WHERE [Student ID]
                                    = '{input_student_id_update}';
                                    """
                                        )
                                connection.commit()
                                # Add up all the details and update student account
                                input(
                                "Full name changed successfully; "\
                                f"\n Username: {no_sp_user_update}"\
                                f"\n Student email: {new_email_update}"
                                "\nPress 'Enter' to procede     "
                                )
                                break
                    elif update_student_action == "2":
                        while True:
                            print(input_student_id_update)
                            # Enrol student with a check to be sure
                            # it's the right student
                            student_enrol_sure = input(
                                "\nAre you sure you would like to enrol this student ? "\
                                "(Enter 'yes' to continue, 'no' to go back): "
                            )
                            if student_enrol_sure == "no":
                                break
                            if student_enrol_sure == "yes":
                                cursor.execute(
                                    f"""UPDATE Enrolment
                                    SET Enrolled = 'Yes'
                                    WHERE [Student ID]
                                    = {input_student_id_update}
                                ;"""
                                )
                                enrol_now = datetime.now()
                                cursor.execute(
                                    f"""UPDATE Enrolment
                                    SET 'Date/Time' 
                                    = '{enrol_now}'
                                    WHERE [Student ID]
                                    = {input_student_id_update}
                                ;"""
                                )
                                connection.commit()
                                print("\nEnrolment complete")
                                break
                            print("\nInput Invalid")
                            continue
                    elif update_student_action == "3":
                        while True:
                            input_course_update = input("\nEnter COURSE ID: ")
                            cursor.execute(
                                f"""SELECT 'Course ID'
                                FROM Courses
                                WHERE EXISTS (SELCT Name
                                FROM Courses
                                WHERE 'Course ID'
                                = '{input_course_update}')"""
                            )  # Update student's course
                            if cursor.fetchall():
                                cursor.execute(
                                    f"""UPDATE Student_Users
                                    SET course_name
                                    = '{input_course_update}'
                                    WHERE Student_ID
                                    = '{input_student_id_update}'"""
                                )
                                connection.commit()
                                break
                            print("\nCourse doesn't exist")
                            continue
                    else:
                    # Return to prompt if input not recognised
                        print("\nInput Invalid")
                        continue

class Teacher:
    ''' Groups every teacher related functions executed by admin '''
    def admin_create_teacher():
        ''' Creates a new teacher account as admin (no arguments necessary) '''
        while True:
            # Create a new teacher account with the possibility to go back or
            # to procede
            ipt_create_t_sure = input(
                "\nPress 'Enter' to procede, enter 'Return' to exit: "
            )
            if ipt_create_t_sure == "Return":
                break
            if ipt_create_t_sure == "":
                while True:
                    # Add full name and thus make a username and a teacher
                    # email, add a title and a course
                    ipt_first_name_t = input(
                        "\nPlease enter 'First Name'(lowercase only): "
                    )
                    if (
                        isNumeric(ipt_first_name_t)
                        or not isspace_and_alpha(ipt_first_name_t)
                        or isUppercase(ipt_first_name_t)
                    ):
                        print(
                            "\nInput invalid (Use letters in lowercase only)"
                        )
                        continue
                    if not len(ipt_first_name_t) > 1:
                        print("\nInput Invalid")
                        continue
                    ipt_last_name_t = input(
                        "\nPlease enter 'Last Name'(lowercase only): "
                    )
                    if (
                        isNumeric(ipt_last_name_t)
                        or not isspace_and_alpha(ipt_last_name_t)
                        or isUppercase(ipt_last_name_t)
                    ):
                        print(
                            "\nInput invalid (Use letters in lowercase only)"
                        )
                        continue
                    if not len(ipt_last_name_t) > 1:
                        print("\nInput Invalid")
                        continue
                    first_ltrs_t = ipt_first_name_t[0:5]
                    last_ltrs_t = ipt_last_name_t[0:4]
                    while True:
                        n5 = random.randint(0, 9)
                        first_n_t = str(n5)
                        n6 = random.randint(0, 9)
                        second_n_t = str(n6)
                        n7 = random.randint(0, 9)
                        third_n_t = str(n7)
                        n8 = random.randint(0, 9)
                        last_n_t = str(n8)
                        new_user_t = (
                            first_ltrs_t
                            + last_ltrs_t
                            + first_n_t
                            + second_n_t
                            + third_n_t
                            + last_n_t
                        )
                        no_space_user_t = new_user_t.replace(" ", "_")
                        cursor.execute(
                            f"""SELECT User
                            FROM Teacher_Users 
                            WHERE EXISTS (SELECT * 
                            FROM Teacher_Users 
                            WHERE User = '{no_space_user_t}');"""
                        )
                        # Redo number assortment if username already exists
                        if cursor.fetchall():
                            continue
                        break
                    new_first_name_t = ipt_first_name_t.title()
                    new_last_name_t = ipt_last_name_t.title()
                    new_email_t = no_space_user_t + "@coventry.ac.uk"
                    t_full_name = new_first_name_t + " " + new_last_name_t
                    ipt_t_course = input("\nEnter COURSE ID: ")
                    cursor.execute(
                        f"""SELECT [Course ID]
                        FROM Courses
                        WHERE EXISTS (SELECT *
                        FROM Courses
                        WHERE [Course ID]
                        = '{ipt_t_course}');"""
                    )
                    if cursor.fetchall():
                        course_name_t = cursor.execute(
                            f"""SELECT Name
                            FROM Courses
                            WHERE [Course ID]
                            = '{ipt_t_course}';"""
                        )  # To get the name of the course and
                           # reinject it in teacher_User database
                        t_course = course_name_t.fetchone()
                        sql_t_course = t_course[0]
                        ipt_t_tle = input(
                            "\nEnter teacher title (Course Leader or Tutor): "
                        )
                        t_tle = ipt_t_tle.title()
                        if ipt_t_tle != [
                            "course leader",
                            "tutor",
                            "Course leader",
                            "Tutor",
                            "Course Leader",
                        ]:
                            print("\nTitle recognised")
                        else:
                            print("\nTitle not recognised")
                            continue
                        cursor.execute(
                            f"""INSERT INTO Teacher_Users
                            (
                            First_Name,
                            Last_Name,
                            Course,
                            Title,
                            User
                            )
                            VALUES
                            (
                            '{new_first_name_t}',
                            '{new_last_name_t}',
                            '{sql_t_course}',
                            '{t_tle}',
                            '{new_user_t}'
                            );"""
                        )
                        connection.commit()
                        teacherid = cursor.execute(
                            f"""SELECT Teacher_ID
                            FROM Teacher_Users
                            WHERE User
                            = '{new_user_t}';"""
                        ) # To get the teacher_id and
                          # reinject it in teacher_Username database
                        t_id = teacherid.fetchone()
                        sql_t_id = t_id[0]
                        cursor.execute(
                            f"""INSERT INTO Teacher_Username
                            ([Teacher ID],
                            Username,
                            [Full Name],
                            Email)
                            VALUES
                            ('{sql_t_id}',
                            '{new_user_t}',
                            '{t_full_name}',
                            '{new_email_t}')
                            ;"""
                        )
                        connection.commit()
                        # Add up all the values and create new teacher account
                        print("\nTeacher added successfully")
                        break
                    # Check if course exists if not returns
                    # to previous prompt
                    print("\nCourse doesn't exist")
                    continue

    def admin_delete_teacher():
        ''' Deletes an existing teacher account as admin (no arguments necessary) '''
        while True:
            # Delete a teacher account and give the possibility to go back
            input_delete_teacher_sure = input(
                "\nPress 'Enter' to procede, enter 'Return' to exit: "
            )
            if input_delete_teacher_sure == "Return":
                break
            if input_delete_teacher_sure == "":
                while True:
                    teacher_id_delete = input(
                        "\nInput the Teacher ID of the teacher account to delete: "
                    )
                    print(f"\n{teacher_id_delete}")
                    # To be sure it's the right teacher
                    teacher_deletion_sure = input(
                        "\nAre you sure you want to delete this account ? "\
                        "(Enter 'yes' to continue, 'no' to go back): ",
                    )
                    if teacher_deletion_sure == "no":
                        break
                    if teacher_deletion_sure == "yes":
                        cursor.execute(
                            f"""SELECT Teacher_ID
                                       FROM Teacher_Users 
                                       WHERE EXISTS (SELECT Teacher_ID
                                       FROM Teacher_Users
                                       WHERE Teacher_ID
                                       = '{teacher_id_delete}');"""
                        )
                        if cursor.fetchall():
                            cursor.execute(
                                f"""DELETE
                                FROM Teacher_Users 
                                WHERE Teacher_ID
                                = '{teacher_id_delete}';"""
                            )
                            connection.commit()
                            cursor.execute(
                                f"""DELETE
                                FROM Teacher_Username
                                WHERE [Teacher ID]
                                = '{teacher_id_delete}';"""
                            )
                            connection.commit() 
                            # Teacher account deletion
                            print("\nDeletion Successful")
                            break
                        # Return to previous prompt if account not found
                        print("\nTeacher account not found")
                        continue
                    else:
                        # Returns to previous prompt if input not recognised
                        print("\nInput Invalid")
                        continue

    def admin_update_teacher():
        ''' Updates an existing teacher account as admin (no arguments necessary) '''
        while True:
            # Update a teacher account and give the possibility to go back
            ipt_delete_t_sure = input(
                "\nPress 'Enter' to procede, enter 'Return' to exit: "
            )
            if ipt_delete_t_sure == "Return":
                break
            if ipt_delete_t_sure == "":
                while True:
                    # Get Teacher ID and continue if it exists in database
                    ipt_t_id_upd = input(
                        "\nYou have chosen to update a teacher account, "\
                        "enter the TEACHER ID of the teacher account you wish to update: "\
                        "\n(Enter 'Return' to exit)             "
                    )
                    if ipt_t_id_upd == 'Return':
                        print("Exit successful")
                        break
                    print(ipt_t_id_upd)
                    # To be sure it's the right student
                    student_deletion_sure = input(
                        "\nAre you sure you want to update this account ? "\
                        "(Enter 'yes' to continue, 'no' to go back): "
                    )
                    if student_deletion_sure == "no":
                        break
                    if student_deletion_sure == "yes":
                        cursor.execute(
                            f"""SELECT Teacher_ID
                            FROM Teacher_Users 
                            WHERE EXISTS (SELECT Teacher_ID 
                            FROM Teacher_Users 
                            WHERE Teacher_ID 
                            = '{ipt_t_id_upd}');"""
                        )
                        if not cursor.fetchall():
                            print("\nTeacher not found")
                            continue
                        upd_t_action = input(
                            "\nWhat do you wish to update: "\
                            "\n 1. Full name,"\
                            "\n 2. Title,"\
                            "\n 3. Course: "
                        )
                        if upd_t_action == "1":
                            while True:
                                ipt_first_name_t_upd = input(
                                    "\nPlease enter 'First Name'(lowercase only): "
                                )
                                if (
                                    isNumeric(ipt_first_name_t_upd)
                                    or not isspace_and_alpha(ipt_first_name_t_upd)
                                    or isUppercase(ipt_first_name_t_upd)
                                ):
                                    print(
                                        "\nInput invalid ",
                                        "(Use letters in lowercase only)"
                                    )
                                    continue
                                if not len(ipt_first_name_t_upd) > 1:
                                    print("\nInput Invalid")
                                    continue
                                ipt_last_name_t_upd = input(
                                    "\nPlease enter 'Last Name'(lowercase only): "
                                )
                                if (
                                    isNumeric(ipt_last_name_t_upd)
                                    or not isspace_and_alpha(
                                        ipt_last_name_t_upd
                                    )
                                    or isUppercase(ipt_last_name_t_upd)
                                ):
                                    print(
                                        "\nInput invalid",
                                        "(Use letters in lowercase only)"
                                    )
                                    continue
                                if not len(ipt_last_name_t_upd) > 1:
                                    print("\nInput Invalid")
                                    continue
                                first_ltrs_t_upd = (
                                    ipt_first_name_t_upd[0:5]
                                )
                                last_ltrs_t_upd = (
                                    ipt_last_name_t_upd[0:4]
                                )
                                while True:
                                    number5_upd = random.randint(
                                        0, 9
                                    )
                                    first_number_t_upd = str(
                                        number5_upd
                                    )
                                    number6_upd = random.randint(
                                        0, 9
                                    )
                                    scnd_number_t_upd = str(
                                        number6_upd
                                    )
                                    number7_upd = random.randint(
                                        0, 9
                                    )
                                    third_number_t_upd = str(
                                        number7_upd
                                    )
                                    number8_upd = random.randint(
                                        0, 9
                                    )
                                    last_number_t_upd = str(
                                        number8_upd
                                    )
                                    new_user_t_upd = (
                                        first_ltrs_t_upd
                                        + last_ltrs_t_upd
                                        + first_number_t_upd
                                        + scnd_number_t_upd
                                        + third_number_t_upd
                                        + last_number_t_upd
                                    )
                                    no_space_t_user_upd = (
                                        new_user_t_upd.replace(
                                            " ", "_"
                                        )
                                    )
                                    cursor.execute(
                                        f"""SELECT User
                                            FROM Teacher_Users 
                                            WHERE EXISTS (SELECT * 
                                            FROM Teacher_Users 
                                            WHERE User 
                                            = '{no_space_t_user_upd}');"""
                                    )  # Redo assortment if username already exists
                                    if cursor.fetchall():
                                        continue
                                    break
                                new_first_name_t_upd = (
                                    ipt_first_name_t_upd.title()
                                )
                                new_last_name_t_upd = (
                                    ipt_last_name_t_upd.title()
                                )
                                new_email_t_upd = (
                                    no_space_t_user_upd
                                    + "@coventry.ac.uk"
                                )
                                t_full_name_upd = (
                                    new_first_name_t_upd + " " + new_last_name_t_upd
                                )
                                cursor.execute(
                                    f"""UPDATE Teacher_Users
                                        First_Name
                                        = '{new_first_name_t_upd}',
                                        Last_Name
                                        = '{new_last_name_t_upd}',
                                        WHERE Teacher_ID
                                        = '{ipt_t_id_upd}';"""
                                )
                                connection.commit()
                                cursor.execute(
                                    f"""UPDATE Teacher_Username
                                        SET Username
                                        = '{new_user_t_upd}',
                                        [Full Name]
                                        = '{t_full_name_upd}',
                                        Email
                                        = '{new_email_t_upd}'
                                        WHERE [Teacher ID]
                                        = '{ipt_t_id_upd}';"""
                                )
                                connection.commit()
                                input(
                                    "Full name changed successfully; "\
                                    f"\n Username: {no_space_t_user_upd}"\
                                    f"\n Teacher email: {new_email_t_upd}"\
                                    "\nPress 'Enter' to procede     "
                                      )
                                # Update full name thus update teacher email and username as well
                                break
                        elif upd_t_action == "2":
                            while True:
                                # Update teacher title with only Course
                                # Leader and Tutor as possible input
                                # options
                                tle_upd = input(
                                    "\nEnter a title (Course Leader or Tutor): "
                                )
                                title_tle_upd = tle_upd.title()
                                if title_tle_upd == "Course Leader":
                                    cursor.execute(
                                        """UPDATE Teacher_Users 
                                        SET Title = 'Course Leader';"""
                                    )
                                    connection.commit()
                                    print("\nTitle updated successfully")
                                    break
                                if title_tle_upd == "Tutor":
                                    cursor.execute(
                                        """UPDATE Teacher_Users 
                                        SET Title = 'Tutor';"""
                                    )
                                    connection.commit()
                                    print("\nTitle updated successfully")
                                    break
                                print("\nInput Invalid")
                                continue
                        elif upd_t_action == "3":
                            while True:
                                ipt_course_upd = input("\nEnter COURSE ID: ")
                                cursor.execute(
                                    f"""SELECT [Course ID]
                                               FROM Courses 
                                               WHERE EXISTS (SELECT Name 
                                               FROM Courses 
                                               WHERE [Course ID]
                                               = '{ipt_course_upd}');"""
                                )  # Update Teacher's course by using Course ID in Courses database
                                if cursor.fetchall():
                                    t_upd_course_name_csr = cursor.execute(
                                        """SELECT Name 
                                        FROM Courses"""
                                    )
                                    t_upd_course_name = (
                                        t_upd_course_name_csr.fetchone()
                                    )
                                    sql_course_nut = t_upd_course_name[0]
                                    cursor.execute(
                                        f"""UPDATE Teacher_Users
                                                   SET Course = '{
                                                   sql_course_nut}'
                                                   WHERE Teacher_ID = '{ipt_t_id_upd}';"""
                                    )
                                    connection.commit()
                                    break
                                print("\nCourse doesn't exist")
                                continue
                        else:
                            # Returns to previous prompt if input not
                            # recognised
                            print("\nInput Invalid")
                            continue
