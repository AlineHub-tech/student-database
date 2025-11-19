students = []

def add_student():
    name = input("Enter student name: ")
    age = input("Enter age: ")
    student_id = input("Enter student ID: ")

    student = {
        "name": name,
        "age": age,
        "id": student_id
    }
    students.append(student)
    save_to_file()
    print("Student added successfully!\n")


def view_students():
    print("\n=== STUDENT DATABASE ===")
    for s in students:
        print(f"Name: {s['name']}, Age: {s['age']}, ID: {s['id']}")
    print()


def delete_student():
    sid = input("Enter ID to delete: ")

    for s in students:
        if s["id"] == sid:
            students.remove(s)
            save_to_file()
            print("Student removed!\n")
            return

    print("Student not found!\n")


def save_to_file():
    with open("students.txt", "w") as file:
        for s in students:
            line = f"{s['name']},{s['age']},{s['id']}\n"
            file.write(line)


def load_from_file():
    try:
        with open("students.txt", "r") as file:
            for line in file:
                name, age, sid = line.strip().split(",")
                students.append({"name": name, "age": age, "id": sid})
    except FileNotFoundError:
        pass


def menu():
    load_from_file()

    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            break
        else:
            print("Invalid choice!\n")



menu()
