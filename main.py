from operation.add import add_student;
from operation.delete import delete_student;
from operation.show import show_students;
from operation.specific import specific_student;


import csv

def main():
    with open('student.csv', mode='w', newline='') as f:
        fields = input("enter the heading which you want separated by comma: ").split(',')
        writer = csv.writer(f)
        writer.writerow(fields)
    while True:
        x = input(
            "what did you want to do\n"
            "1 for add student\n"
            "2 for delete student\n"
            "3 for see students data\n"
            "4 for see marks for a specific student\n"
            "enter any other input for exit\n"
        )
        if x == "1":
            add_student()
        elif x == "2":
            delete_student()
        elif x == "3":
            show_students()
        elif x == "4":
            specific_student()
        else:
            print("exiting")
            exit(0)

if __name__ == "__main__":
    main()