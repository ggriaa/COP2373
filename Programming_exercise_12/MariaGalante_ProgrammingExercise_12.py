"""
Maria Galante
COP2373
Programming Exercise #12

This program uses NumPy to read student grade data from a CSV file.
It analyzes exam scores by calculating statistics for each exam,
including mean, median, standard deviation, minimum, and maximum.
It also calculates overall statistics for all exams combined,
determines how many students passed or failed each exam, and
calculates the overall pass percentage.

Student: Maria Galante
Date: 2026-04-15
"""

import numpy as np


def load_grades(filename):
    """
    Load exam grade columns from the CSV file.

    Parameter:
        filename (str): Name of the CSV file.

    Return:
        numpy.ndarray: Array containing exam grades.
    """

    # Load exam score columns from the CSV file.
    data = np.genfromtxt(
        filename,
        delimiter=",",
        skip_header=1,
        usecols=(2, 3, 4)
    )

    return data


def exam_statistics(data):
    """
    Display statistics for each exam column.

    Parameter:
        data (numpy.ndarray): Array of exam grades.
    """

    print("----- Exam Statistics -----")

    # Loop through each exam column.
    for index in range(data.shape[1]):
        exam = data[:, index]

        print(f"\nExam {index + 1}")
        print("Mean:", round(np.mean(exam), 2))
        print("Median:", round(np.median(exam), 2))
        print("Standard Deviation:", round(np.std(exam), 2))
        print("Minimum:", np.min(exam))
        print("Maximum:", np.max(exam))


def overall_statistics(data):
    """
    Display statistics for all exams combined.

    Parameter:
        data (numpy.ndarray): Array of exam grades.
    """

    # Flatten array into one list of all scores.
    all_scores = data.flatten()

    print("\n----- Overall Statistics -----")
    print("Mean:", round(np.mean(all_scores), 2))
    print("Median:", round(np.median(all_scores), 2))
    print("Standard Deviation:", round(np.std(all_scores), 2))
    print("Minimum:", np.min(all_scores))
    print("Maximum:", np.max(all_scores))


def pass_fail(data):
    """
    Display pass/fail totals for each exam and overall pass percentage.

    Parameter:
        data (numpy.ndarray): Array of exam grades.
    """

    print("\n----- Pass / Fail by Exam -----")

    # Check each exam column for passing and failing grades.
    for index in range(data.shape[1]):
        exam = data[:, index]

        passed = np.sum(exam >= 60)
        failed = np.sum(exam < 60)

        print(f"\nExam {index + 1}")
        print("Passed:", passed)
        print("Failed:", failed)

    # Count all passing grades in the dataset.
    total_scores = data.size
    total_passed = np.sum(data >= 60)

    pass_percent = (total_passed / total_scores) * 100

    print("\nOverall Pass Percentage:",
          round(pass_percent, 2), "%")


def main():
    """
    Run the program.
    """

    filename = "grades.csv"

    # Load grades from file.
    data = load_grades(filename)

    print("----- First Few Rows -----")
    print(data[:5])

    exam_statistics(data)
    overall_statistics(data)
    pass_fail(data)


# Run program when file is executed directly.
if __name__ == "__main__":
    main()