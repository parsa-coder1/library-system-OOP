import json

from models import Book, User

from helpers import find_book_by_id

def save_data(library):

    data = {
        "books": [book.to_dict() for book in library.books],
        "users": [user.to_dict() for user in library.users]
    }

    with open("library_data.json", "w") as file:
        json.dump(data, file, indent=4)


def load_data(library):

    try:

        with open("library_data.json", "r") as file:
            data = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return
        
    library.books.clear()
    library.users.clear()

    for book_data in data["books"]:

        book = Book(
            book_data["id"],
            book_data["title"],
            book_data["author"]
        )

        book.available = book_data["available"]

        library.books.append(book)

    for user_data in data["users"]:

        user = User(
            user_data["id"],
            user_data["name"]
        )

        for book_id in user_data["borrowed_books"]:

            found_book = find_book_by_id(library.books, book_id)

            if found_book:
                user.borrowed_books.append(found_book)

        library.users.append(user)


    # manage next id

    if library.books:
        library.next_book_id = max(book.id for book in library.books) + 1

    if library.users:
        library.next_user_id = max(user.id for user in library.users) + 1
