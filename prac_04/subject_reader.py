"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subjects = load_subjects()
    display_subjects(subjects)


def load_subjects():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subjects = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subjects.append(parts)

    input_file.close()
    return subjects


def display_subjects(subjects):
    """Display data nicely."""
    for subject in subjects:
        # Print using the format method and *unpacking
        print(f"{subject[0]} is taught by {subject[1]:12} and has {subject[2]:3} students")


main()