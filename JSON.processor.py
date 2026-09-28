import json

# Sample student data
students = [
    {
        "name": "Sandeep",
        "age": 20,
        "course": "B.Tech",
        "marks": 85
    },
    {
        "name": "Rahul",
        "age": 21,
        "course": "BCA",
        "marks": 72
    },
    {
        "name": "Aman",
        "age": 20,
        "course": "B.Tech",
        "marks": 90
    },
    {
        "name": "Priya",
        "age": 21,
        "course": "BCA",
        "marks": 65
    }
]

# Create JSON file
with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

# Read JSON file
with open("students.json", "r") as file:
    students = json.load(file)

print("===== JSON DATA PROCESSOR =====")

while True:

    print("\n1. Display All Students")
    print("2. Search Student")
    print("3. Filter by Course")
    print("4. Show Summary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        for student in students:
            print(student)

    elif choice == "2":

        name = input("Enter student name: ")

        found = False

        for student in students:
            if student["name"].lower() == name.lower():
                print("Student Found:")
                print(student)
                found = True

        if found == False:
            print("Student not found.")

    elif choice == "3":

        course = input("Enter course: ")

        found = False

        for student in students:
            if student["course"].lower() == course.lower():
                print(student)
                found = True

        if found == False:
            print("No student found.")

    elif choice == "4":

        total = len(students)

        total_marks = 0

        for student in students:
            total_marks = total_marks + student["marks"]

        average = total_marks / total

        print("\n===== SUMMARY =====")
        print("Total Students:", total)
        print("Average Marks:", average)

    elif choice == "5":

        print("Program ended.")
        break

    else:

        print("Invalid choice!")