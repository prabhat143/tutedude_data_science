#!/usr/bin/env python3
"""
Employee Management System (EMS)
- Stores employee data in a dictionary of dictionaries
- Demonstrates control structures, functions, and basic OOP-friendly organization
"""

from typing import Dict, Any

# -------------------------------
# Step 1 - Data Storage (Seeded)
# -------------------------------

employees: Dict[int, Dict[str, Any]] = {
    101: {"name": "Satya", "age": 27, "department": "HR", "salary": 50000},
    102: {"name": "Anita", "age": 31, "department": "Finance", "salary": 68000},
    103: {"name": "Rohit", "age": 24, "department": "Engineering", "salary": 72000},
}


# -------------------------------
# Helpers
# -------------------------------

def input_int(prompt: str) -> int:
    """Get an integer from input with validation loop."""
    while True:
        val = input(prompt).strip()
        if val.isdigit() or (val.startswith('-') and val[1:].isdigit()):
            try:
                return int(val)
            except ValueError:
                pass
        print("Invalid input. Please enter a valid integer.")


def input_positive_int(prompt: str) -> int:
    """Get a positive integer from input with validation loop."""
    while True:
        n = input_int(prompt)
        if n > 0:
            return n
        print("Please enter a positive integer.")


def input_float(prompt: str) -> float:
    """Get a floating-point number from input with validation loop."""
    while True:
        val = input(prompt).strip()
        try:
            return float(val)
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def print_table(data: Dict[int, Dict[str, Any]]) -> None:
    """Pretty-print the employees dict in a table-like format."""
    if not data:
        print("No employees available.")
        return

    headers = ["ID", "Name", "Age", "Department", "Salary"]
    rows = []
    for emp_id, details in sorted(data.items(), key=lambda x: x[0]):
        rows.append([emp_id, details["name"], details["age"], details["department"], details["salary"]])

    # Column widths
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))

    def fmt_row(r):
        return " | ".join(str(c).ljust(col_widths[i]) for i, c in enumerate(r))

    # Print header
    print(fmt_row(headers))
    print("-+-".join("-" * w for w in col_widths))

    # Print rows
    for row in rows:
        # Format salary to 2 decimals
        row = list(row)
        row[4] = f"{float(row[4]):.2f}"
        print(fmt_row(row))


# -------------------------------
# Step 3 - Add Employee
# -------------------------------

def add_employee() -> None:
    print("\n=== Add Employee ===")
    while True:
        emp_id = input_positive_int("Enter Employee ID (integer): ")
        if emp_id in employees:
            print(f"Employee ID {emp_id} already exists. Please choose a different ID.")
        else:
            break

    name = input("Enter Employee Name: ").strip()
    while not name:
        print("Name cannot be empty.")
        name = input("Enter Employee Name: ").strip()

    age = input_positive_int("Enter Employee Age: ")
    department = input("Enter Department: ").strip()
    while not department:
        print("Department cannot be empty.")
        department = input("Enter Department: ").strip()

    salary = input_float("Enter Monthly Salary: ")

    employees[emp_id] = {
        "name": name,
        "age": age,
        "department": department,
        "salary": salary,
    }
    print(f"Employee {name} (ID: {emp_id}) added successfully!\n")


# -------------------------------
# Step 4 - View All Employees
# -------------------------------

def view_employees() -> None:
    print("\n=== All Employees ===")
    print_table(employees)
    print()


# -------------------------------
# Step 5 - Search Employee by ID
# -------------------------------

def search_employee() -> None:
    print("\n=== Search Employee ===")
    emp_id = input_positive_int("Enter Employee ID to search: ")
    if emp_id in employees:
        details = employees[emp_id]
        print("\nEmployee Found:")
        print(f"ID         : {emp_id}")
        print(f"Name       : {details['name']}")
        print(f"Age        : {details['age']}")
        print(f"Department : {details['department']}")
        print(f"Salary     : {float(details['salary']):.2f}\n")
    else:
        print("Employee not found.\n")


# -------------------------------
# Step 2 & 6 - Menu & Exit
# -------------------------------

def main_menu() -> None:
    while True:
        print("==== Employee Management System (EMS) ====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            print("Thank you for using the EMS. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.\n")


if __name__ == "__main__":
    main_menu()
