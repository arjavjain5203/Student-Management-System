import csv

def search_name():
    with open('student.csv', mode='r', newline='') as f:
        name = input("Enter the name of the student you want to see: ")
        reader = csv.reader(f)
        data = list(reader) 

    name_index = -1

    # Find the index of the 'name' column
    for i, col in enumerate(data[0]):
        if col.lower() == 'name':
            name_index = i
            break

    if name_index == -1:
        print("No 'Name' column found.")
        return

    for row in data[1:]: 
        if row[name_index] == name:
            print(f'details of the selected student is {row}')          



def search_roll():
    with open('student.csv', mode='r', newline='') as f:
        roll = input("Enter the roll number of the student you want to see: ")
        reader = csv.reader(f)
        data = list(reader) 

    name_index = -1

    # Find the index of the 'roll' column
    for i, col in enumerate(data[0]):
        if col.lower() == 'roll':
            name_index = i
            break

    if name_index == -1:
        print("No 'roll number' column found.")
        return


    for row in data[1:]:  # skip header
        if row[name_index] == roll:
            print(f'details of the specific stident is {row}')

    
    
    
    
def specific_student():
    while True:
        x = input("How do you want to search the student? \n1 for by name \n2 for roll number \n3 to exit\n")
        try:
            x = int(x)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if x == 1:
            search_name()
        elif x == 2:
            search_roll()
        elif x == 3:
            print("Exit")
            break
        else:
            print("You did not enter a valid input.")