from models import list_students;

def show_registration_students():
    print("Registration Student")
    print("======================")

    for student in list_students:
        print(student)