''' Imports SQLite3 so that I can use the database (school.db) in my program  '''
import sqlite3

from isAny import isUCAS_codes_approved, isspace_and_alpha

# explained in file

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

class Course:
    ''' Groups every course related functions '''
    def admin_create_course():
        ''' Creates a new course (no arguments necessary) '''
        while True:
            create_course_admin = input(
                "\nPress 'Enter' to procede, input 'Return' to exit: "
            )  # Give the possibility to exit if it was a missclick
            if create_course_admin == "Return":
                print("\nExit successful")
                break
            if create_course_admin == "":
                while True:
                    new_name = input(
                        "\nInput a new name for the course selected: "
                    )
                    if not isspace_and_alpha(new_name):
                        print("\nInput Invalid")
                        continue
                    break
                while True:
                    new_duration = input(
                        "\nInput the duration of the selected course: "
                    )
                    if not new_duration.isnumeric():
                        print("\nInput Invalid")
                        continue
                    break
                while True:
                    new_degree = input(
                        "\nInput degree level"\
                        " (BSc, Beng, MSCi,... etc.): "
                    )
                    if new_degree not in (
                        "BA",
                        "BEng",
                        "MEng",
                        "BSc",
                        "MSCi",
                        "BEng/MEng",
                        "BSc/MSCi",
                        "MChem",
                        "LLB",
                        "LLB/LLM",
                        "MA",
                        "MBA",
                        "MPhil",
                        "MRes",
                        "LLM",
                        "PhD",
                        "MArts",
                        "MBiol",
                        "MComp",
                        "MMath",
                        "MPhys",
                    ):
                        print("\nInput Invalid")
                        continue
                    break
                while True:
                    new_mode = input(
                        "\nInput the study mode(s) "\
                        "\n(F-T, F-T/S, F-T/O/B): "
                    )
                    if new_mode not in (
                        "F-T",
                        "F-T/S",
                        "F-T/O/B",
                    ):
                        print("\nInput Invalid")
                        continue
                    break
                while True:
                    new_foundation_input = input(
                        "\nFoundation year availability; Input: "\
                        "\n 0 if unavailable, "\
                        "\n 1 if available: "
                    )
                    if new_foundation_input == "1":
                        new_foundation = "Available"
                        break
                    if new_foundation_input == "0":
                        new_foundation = "Unavailable"
                        break
                    print("\nInput Invalid")
                    continue
                while True:
                    new_placement_input = input(
                        "\nPlacement year availability; Input: "\
                        "\n 0 if unavailable, "\
                        "\n 1 if available: "
                    )
                    if new_placement_input == "1":
                        new_placement = "Available"
                        break
                    if new_placement_input == "0":
                        new_placement = "Unavailable"
                        break
                    print("\nInput Invalid")
                    continue
                while True:
                    new_industrial_input = input(
                        "\nIndustrial year availability; Input:"\
                        "\n 0 if unavailable, "\
                        "\n 1 if available: "
                    )
                    if new_industrial_input == "1":
                        new_industrial = "Available"
                        break
                    if new_industrial_input == "0":
                        new_industrial = "Unavailable"
                        break
                    print("\nInput Invalid")
                    continue
                while True:
                    new_ucas = input(
                        "\nEnter course UCAS codes: "
                    )
                    code_ucas = new_ucas.capitalize
                    if len(
                        new_ucas
                    ) != 4 and not isUCAS_codes_approved(
                        code_ucas
                    ):
                        print("\nInput Invalid")
                        continue
                    cursor.execute(
                        f"""INSERT INTO Courses
                        (Name, 
                        [Duration (year)], 
                        Degree, 
                        [Study Mode], 
                        [Foundation Year], 
                        [Placement Year], 
                        [Industrial Year], 
                        [UCAS CODES]) 
                        VALUES 
                        ('{new_name}',
                        '{new_duration}',
                        '{new_degree}',
                        '{new_mode}',
                        '{new_foundation}',
                        '{new_placement}',
                        '{new_industrial}',
                        '{new_ucas}');"""
                    )  # Add up every value a create a new course
                    connection.commit()
                    print("\nCourse added successfully")
                    break
            else:
                print(
                    "\nInput Invalid"
                )  # If input not recognized
                continue

    def admin_update_course():
        ''' Updates an existing course (no arguments necessary) '''
        while True:
            modified_course_id = input(
                "Input the COURSE ID of the course to be modified:"\
                "\n (Enter 'Return' to exit)"\
                "\n (Press 'Enter' to keep previous info)  "
            )  # To update an already existing course
            if modified_course_id == "Return":
                print("\nExit successful")
                break
            cursor.execute(
                f"""SELECT [Course ID]
                FROM Courses 
                WHERE NOT EXISTS (SELECT * 
                FROM Courses 
                WHERE [Course ID] 
                = '{modified_course_id}');"""
            )
            if cursor.fetchall():
                print("\nCourse does not exist.")
                continue
            while True:
                new_name = input(
                    "\nInput a new name for the course selected: "
                )
                if new_name == "":
                    pass
                else:
                    cursor.execute(
                        f"""UPDATE Courses
                        SET Name 
                        = '{new_name}'
                        WHERE [Course ID] 
                        = '{modified_course_id}';"""
                    )
                    connection.commit()
                    break
            while True:
                new_duration = input(
                    "\nInput the duration of the selected course: "
                )
                if new_duration == "":
                    break
                cursor.execute(
                    f"""UPDATE Courses
                    SET [Duration (year)] 
                    = '{new_duration}'
                    WHERE [Course ID] 
                    = '{modified_course_id}';"""
                )
                connection.commit()
                break
            while True:
                new_degree = input(
                    "\nInput degree level "\
                    "(BSc, Beng, MSCi,... etc.): "
                )
                if new_degree == "":
                    break
                if new_degree not in (
                    "BA",
                    "BA",
                    "BEng",
                    "MEng",
                    "BSc",
                    "MSCi",
                    "BEng/MEng",
                    "BSc/MSCi",
                    "MChem",
                    "LLB",
                    "LLB/LLM",
                    "MA",
                    "MBA",
                    "MPhil",
                    "MRes",
                    "LLM",
                    "PhD",
                    "MArts",
                    "MBiol",
                    "MComp",
                    "MMath",
                    "MPhys",
                    ):
                    print("\nInput Invalid")
                    continue
                cursor.execute(
                    f"""UPDATE Courses
                    SET Degree 
                    = '{new_degree}'
                    WHERE [Course ID] 
                    = '{modified_course_id}';"""
                )
                connection.commit()
                break
            while True:
                new_mode = input(
                    "\nInput the study mode(s)"\
                    " (F-T, F-T/S, F-T/O/B): "
                )
                if new_mode == "":
                    break
                if new_mode not in (
                    "F-T",
                    "F-T/S",
                    "F-T/O/B",
                ):
                    print("\nInput Invalid")
                    continue
                cursor.execute(
                    f"""UPDATE Courses
                    SET [Study Mode] 
                    = '{new_mode}'
                    WHERE [Course ID] 
                    = '{modified_course_id}';"""
                )
                connection.commit()
                break
            while True:
                new_foundation = input(
                    "\nFoundation year availability; Input:"\
                    "\n 0 if unavailable, "\
                    "\n 1 if available: "
                )
                if new_foundation == "":
                    break
                if new_foundation == "1":
                    cursor.execute(
                        f"""UPDATE Courses
                        SET [Foundation Year] = 'Available' 
                        WHERE [Course ID] 
                        = '{modified_course_id}';"""
                    )
                    connection.commit()
                    break
                if new_foundation == "0":
                    cursor.execute(
                        f"""UPDATE Courses
                        SET [Foundation Year] = 'Unavailable' 
                        WHERE [Course ID] 
                        = '{modified_course_id}';"""
                    )
                    connection.commit()
                    break
                print("\nInput Invalid")
                continue
            while True:
                new_placement = input(
                    "\nPlacement year availability; Input: "\
                    "\n 0 if unavailable,"\
                    "\n 1 if available: "
                )
                if new_placement == "":
                    break
                if new_placement == "1":
                    cursor.execute(
                        f"""UPDATE Courses
                        SET [Placement Year] = 'Available' 
                        WHERE [Course ID] 
                        = '{modified_course_id}';"""
                    )
                    connection.commit()
                    break
                if new_placement == "0":
                    cursor.execute(
                        f"""UPDATE Courses
                        SET [Placement Year] = 'Unavailable' 
                        WHERE [Course ID] 
                        = '{modified_course_id}';"""
                    )
                    connection.commit()
                    break
                print("\nInput Invalid")
                continue
            while True:
                new_industrial = input(
                    "\nIndustrial year availability; Input: "\
                    "\n 0 if unavailable, "\
                    "\n 1 if available: "
                )
                if new_industrial == "":
                    break
                if new_industrial == "1":
                    cursor.execute(
                        f"""UPDATE Courses
                        SET [Industrial Year] = 'Available' 
                        WHERE [Course ID] 
                        = '{modified_course_id}';"""
                    )
                    connection.commit()
                    break
                if new_industrial == "0":
                    cursor.execute(
                        f"""UPDATE Courses
                        SET [Industrial Year] = 'Unavailable' 
                        WHERE [Course ID] 
                        = '{modified_course_id}';"""
                    )
                    connection.commit()
                    break
                print("\nInput Invalid")
                continue
            while True:
                new_ucas = input(
                    "\nEnter course UCAS codes: "
                )
                code_ucas = new_ucas.capitalize()
                if new_ucas == "":
                    break
                if len(
                    code_ucas
                ) == 4 and isUCAS_codes_approved(
                    code_ucas
                ):
                    cursor.execute(
                        f"""UPDATE Courses
                        SET [UCAS CODES] = {new_ucas}
                        WHERE [Course ID] 
                        = '{modified_course_id}'"""
                    )
                    connection.commit()
                    break
                print("\nInput Invalid")
                continue

    def admin_delete_course():
        ''' Deletes an existing course (no arguments necessary) '''
        while True:
            course_delete_input = input(
                "\nEnter the COURSE ID of the course "\
                "you wish to delete:"\
                "\n (Enter 'Return' to exit)        "
            )  # Delete an already existing course
            if course_delete_input == "Return":
                print("\nExit successful")
                break
            cursor.execute(
                f"""SELECT [Course ID]
                FROM Courses 
                WHERE EXISTS (SELECT * 
                FROM Courses 
                WHERE [Course ID] 
                = '{course_delete_input}');"""
            )  # To find the course in the Courses table
            if cursor.fetchall():
                cursor.execute(
                    f"""DELETE
                    FROM Courses 
                    WHERE [Course ID] 
                    = '{course_delete_input}'"""
                )  # Delete the course if found
                connection.commit()
                print("\nDeletion successful")
            else:
                print(
                    "\nInput Invalid"
                )  # Else return to previous prompt
                continue
