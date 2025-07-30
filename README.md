# Student Management System

This is a simple command-line Student Management System written in Python. It allows you to add, delete, view, and search student records stored in a CSV file.

## Features

- **Add Student:** Enter details for a new student and save them to `student.csv`.
- **Delete Student:** Remove a student by name or roll number.
- **Show Students:** Display all student records.
- **Search Student:** Find a student by name or roll number.

## File Structure

- `main.py` - Entry point for the application.
- `student.csv` - Stores student data.
- `operation/`
  - `add.py` - Functionality to add students.
  - `delete.py` - Functionality to delete students.
  - `show.py` - Functionality to display all students.
  - `specific.py` - Functionality to search for a specific student.

## Getting Started

1. **Install Python 3.**  
2. **Clone this repository.**
3. **Run the program:**
   ```sh
   python main.py
   ```
4. **Follow the prompts in the terminal.**

## Usage

- On startup, enter the column headings you want (e.g., `name,roll,marks`).
- Choose an operation from the menu:
  - `1` - Add student
  - `2` - Delete student
  - `3` - Show all students
  - `4` - Search for a specific student
  - Any other input - Exit


## License

MIT License

---

**Author:**  
Arjav Jain