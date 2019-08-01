from .models import list_books

def run_view():
    print("Books in Library")
    print("======================")

    for book in list_books:
        print(book)