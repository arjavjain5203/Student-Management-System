import csv

def add_student():
    # First read the header to know which fields to ask for
    with open('student.csv', mode='r', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        if not data:
            print("CSV file is empty. Cannot add student.")
            return
        header = data[0]  # First row is header

    # Ask the user for each field value
    new_row = []
    for column_name in header:
        value = input(f"Enter {column_name}: ")
        new_row.append(value)

    # Now append the new row
    with open('student.csv', mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(new_row)

    print("Student added successfully!")
