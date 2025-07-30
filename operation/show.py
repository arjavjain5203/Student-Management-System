import csv

def show_students():
    with open("student.csv",mode='r',newline='') as f:
        reader=csv.reader(f)
        for n in reader:
            print(n)