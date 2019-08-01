from .models import list_students

def run_view():
    print("Registration Student")
    print("======================")

    for student in list_students:
        print(student)