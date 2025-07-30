import csv

def delete_name():
    with open('student.csv', mode='r', newline='') as f:
        name = input("Enter the name of the student you want to delete: ")
        reader = csv.reader(f)
        data = list(reader) 

    if not data:
        print("The file is empty.")
        return

    name_index = -1
    for i, col in enumerate(data[0]):
        if col.lower() == 'name':
            name_index = i
            break

    if name_index == -1:
        print("No 'Name' column found.")
        return

    updated_rows = [data[0]]  # Add header

    found = False
    for row in data[1:]:
        if row[name_index] != name:
            updated_rows.append(row)
        else:
            found = True

    if not found:
        print("No student found with that name.")
        return

    with open('student.csv', mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(updated_rows)
    print(f"Student with name '{name}' deleted successfully.")



def delete_roll():
    with open('student.csv', mode='r', newline='') as f:
        roll = input("Enter the roll number of the student you want to delete: ")
        reader = csv.reader(f)
        data = list(reader)

    if not data:
        print("The file is empty.")
        return

    roll_index = -1
    for i, col in enumerate(data[0]):
        if col.lower() == 'roll':
            roll_index = i
            break

    if roll_index == -1:
        print("No 'Roll' column found.")
        return

    updated_rows = [data[0]]
    found = False
    for row in data[1:]:
        if row[roll_index] != roll:
            updated_rows.append(row)
        else:
            found = True

    if not found:
        print("No student found with that roll number.")
        return

    with open('student.csv', mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(updated_rows)
    print(f"Student with roll number '{roll}' deleted successfully.")


def delete_student():
    while True:
        x = input("How do you want to remove the student? \n1 for by name \n2 for roll number \n3 to exit\n")
        try:
            x = int(x)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if x == 1:
            delete_name()
        elif x == 2:
            delete_roll()
        elif x == 3:
            print("Exit")
            break
        else:
            print("You did not enter a valid input.")
