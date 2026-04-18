"""
MariaGalante_ProgrammingExercise_8.py

This program lets an instructor enter student names and 3 exam grades.
It saves the info into a csv file called grades.csv and then reads the
file back and prints everything in a table format.

Student: Maria Galante
Date: 2026-03-25
"""

# import csv so we can work with csv files easier
import csv


def write_grades():
    """
    Description:
    This function asks how many students the instructor wants to enter.
    Then it gets each student's first name, last name, and 3 exam grades
    and writes the info into grades.csv.

    Parameters:
    None

    Variables:
    num_students (int) - how many students are being entered
    first_name (str) - student's first name
    last_name (str) - student's last name
    exam1 (int) - exam 1 grade
    exam2 (int) - exam 2 grade
    exam3 (int) - exam 3 grade
    file (file object) - file being written to
    writer (csv writer object) - object used to write rows into the csv file

    Steps:
    1. Ask how many students need to be entered.
    2. Open grades.csv in write mode using with.
    3. Write the header row first.
    4. Loop through each student.
    5. Get the student's name and 3 exam grades.
    6. Write each student's record into the file.

    Returns:
    None
    """

    # ask how many students will be entered
    num_students = int(input("How many students do you want to enter? "))

    # open the file in write mode
    # newline="" keeps blank lines from showing up in csv files on Windows
    with open("../Programming_exercise_12/grades.csv", "w", newline="") as file:

        # create csv writer object
        writer = csv.writer(file)

        # write the column headers first
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        # loop once for each student
        for i in range(num_students):

            print("\nEntering info for student", i + 1)

            # get student first name
            first_name = input("Enter first name: ")

            # get student last name
            last_name = input("Enter last name: ")

            # get exam scores
            exam1 = int(input("Enter exam 1 grade: "))
            exam2 = int(input("Enter exam 2 grade: "))
            exam3 = int(input("Enter exam 3 grade: "))

            # write the row to the file
            writer.writerow([first_name, last_name, exam1, exam2, exam3])


def read_grades():
    """
    Description:
    This function reads the grades.csv file and prints everything
    in a table so it is easier to read.

    Parameters:
    None

    Variables:
    file (file object) - file being read
    reader (csv reader object) - object used to read each row
    row (list) - one row from the csv file

    Steps:
    1. Open grades.csv in read mode using with.
    2. Create a csv reader object.
    3. Loop through each row in the file.
    4. Print each row in table format.

    Returns:
    None
    """

    print("\nStudent Grades Table\n")

    # open file in read mode
    with open("../Programming_exercise_12/grades.csv", "r", newline="") as file:

        # create reader object
        reader = csv.reader(file)

        # loop through each row in the file
        for row in reader:

            # print each column spaced out evenly
            print(f"{row[0]:<15}{row[1]:<15}{row[2]:<10}{row[3]:<10}{row[4]:<10}")


def main():
    """
    Description:
    This is the main function for the program.
    It runs the write function first and then the read function.

    Parameters:
    None

    Variables:
    None

    Steps:
    1. Call the function that writes student records to the csv file.
    2. Call the function that reads the csv file and displays the data.

    Returns:
    None
    """

    # write student info into file
    write_grades()

    # now read file and show results
    read_grades()


# start program here
if __name__ == "__main__":
    main()