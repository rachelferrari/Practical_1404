"""Project Management Program
Estimated: 2 hr
Actual:
"""
from project import Project
import datetime

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"

# def main():
#     projects = []
#     print(MENU)
#     choice = input('>>> ')
#     while choice != 'Q':
#         if choice == 'L':
#             load_project()
#
#         elif choice == 'S':
#             pass
#         elif choice == 'D':
#             display_projects()
#
#
#         elif choice == 'F':
#             pass
#         elif choice == 'A':
#             pass
#         elif choice == 'U':
#             pass
#         print(MENU)
#         choice = input('>>> ')
#
# main()

print(MENU)
projects = []
texts = []

with open("projects.txt") as in_file:
    next(in_file)
    for part in in_file:
        parts = part.split()
        parts[:-4] = [' '.join(parts[:-4])]
        texts.append(parts)
        project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), float(parts[4]))
        projects.append(project)

for i in range(len(texts)):
    texts[i][2] = int(texts[i][2])
    texts[i][3] = float(texts[i][3])
    texts[i][4] = float(texts[i][4])

print(texts)

# def load_project():
#     with open("projects.txt") as in_file:
#         next(in_file)
#         for part in in_file:
#             parts = part.split()
#             parts[:-4] = [' '.join(parts[:-4])]
#             texts.append(parts)
#             project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), float(parts[4]))
#             projects.append(project)


def display_projects():
    global line
    print("Incomplete projects:")
    for line in projects:
        if Project.is_not_complete(line):
            print(f"  {line}")
    print("Complete projects: ")
    for line in projects:
        if Project.is_complete(line):
            print(f"  {line}")




count = 0
for line in projects:
    print(f"{count} {line}")
    count += 1

project_choice = int(input("Project choice: "))
print(projects[project_choice])
# new_percentage = float(input("New percentage: "))
# new_priority = int(input("New priority: "))
try:
    new_percentage = float(input("New percentage: "))
    new_priority = int(input("New priority: "))
except ValueError:
    pass
projects[project_choice].change_completion(new_percentage)
print(projects[project_choice])

print("Let's add a new project")
name = input("Name: ")
date_string = input("Date (d/m/yyyy): ")
date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
priority = float(input("Priority: "))
cost = float(input("Cost estimate: $"))
completion = float(input("Percent complete: "))
parts = [name, date_string, priority, cost, completion]
texts.append(parts)
project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
projects.append(project)


# Project(projects[0], projects[1], projects[2], projects[3], projects[4])
