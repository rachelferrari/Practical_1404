"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    # print(data[:-2])
    # for j in range(0, 2):
    #     for i in range(0, 3):
    # for j in range(0, len(data[0]))
    #     print(f"{data[0][0]} is taught by {data[0][1]} and has {data[0][2]} students")
    print_subject_details(data[:-2])


def get_data():
    # """Read data from file formatted like: subject,lecturer,number of students."""
    """Get data and return the data as a list of lists"""
    things = []
    input_file = open(FILENAME)
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        # line = line.strip()  # Remove the \n
        # parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        # parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        # print("----------")
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        things.append(parts)
    return things
    input_file.close()


def print_subject_details(data):
    for i in range(0, len(data)):
        print(f"{data[i][0]} is taught by {data[i][1]} and has {data[i][2]} students")


main()