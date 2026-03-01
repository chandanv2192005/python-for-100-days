# Lesson 12: Mini Project — Student Management System
import os

students = []

def add_student():
    try:
        name  = input("Name: ").strip()
        age   = int(input("Age: "))
        grade = float(input("Grade (0-100): "))
        if not name: raise ValueError("Name empty!")
        if grade < 0 or grade > 100: raise ValueError("Invalid grade!")
        students.append({"name": name, "age": age, "grade": grade,
                         "status": "Pass" if grade >= 50 else "Fail"})
        print(f"Student {name} added!")
    except ValueError as e:
        print(f"Error: {e}")

def view_students():
    if not students: print("No students found!"); return
    print(f"\n{'No.':<5}{'Name':<20}{'Age':<6}{'Grade':<8}{'Status'}")
    print("-" * 50)
    for i, s in enumerate(students, 1):
        print(f"{i:<5}{s['name']:<20}{s['age']:<6}{s['grade']:<8}{s['status']}")

def search_student():
    name = input("Search name: ").strip().lower()
    found = [s for s in students if name in s["name"].lower()]
    if found:
        for s in found: print(s)
    else: print("Not found!")

def update_grade():
    name = input("Student name: ").strip().lower()
    for s in students:
        if s["name"].lower() == name:
            try:
                g = float(input("New grade: "))
                s["grade"]  = g
                s["status"] = "Pass" if g >= 50 else "Fail"
                print("Updated!")
            except ValueError: print("Invalid grade!")
            return
    print("Student not found!")

def delete_student():
    name = input("Name to delete: ").strip().lower()
    for i, s in enumerate(students):
        if s["name"].lower() == name:
            if input(f"Delete {s['name']}? (yes/no): ") == "yes":
                students.pop(i); print("Deleted!")
            return
    print("Not found!")

def save_to_file():
    with open("students.txt", "w") as f:
        for s in students:
            f.write(f"{s['name']},{s['age']},{s['grade']},{s['status']}\n")
    print(f"Saved {len(students)} students.")

def load_from_file():
    if not os.path.exists("students.txt"): return
    students.clear()
    with open("students.txt", "r") as f:
        for line in f:
            p = line.strip().split(",")
            if len(p) == 4:
                students.append({"name": p[0], "age": int(p[1]),
                                 "grade": float(p[2]), "status": p[3]})
    print(f"Loaded {len(students)} students.")

def show_statistics():
    if not students: print("No data!"); return
    grades = [s["grade"] for s in students]
    top    = max(students, key=lambda s: s["grade"])
    print(f"Total: {len(students)}")
    print(f"Average: {sum(grades)/len(grades):.2f}")
    print(f"Top student: {top['name']} ({top['grade']})")

def main_menu():
    load_from_file()
    while True:
        print("\n1.Add  2.View  3.Search  4.Update")
        print("5.Delete  6.Save  7.Load  8.Stats  9.Exit")
        c = input("Choice: ")
        if   c=="1": add_student()
        elif c=="2": view_students()
        elif c=="3": search_student()
        elif c=="4": update_grade()
        elif c=="5": delete_student()
        elif c=="6": save_to_file()
        elif c=="7": load_from_file()
        elif c=="8": show_statistics()
        elif c=="9": save_to_file(); print("Bye!"); break
        else: print("Invalid choice!")

if __name__ == '__main__':
    main_menu()
