
def find_book_by_id(books, book_id):

    for book in books:
        if book.id == book_id:
            return book
        
    return None


def find_user_by_name(users, name):

    for user in users:
        if user.name.lower() == name.lower():
            return user
        
    return None


def find_book_by_title(books, title):

    for book in books:
        if book.title.lower() == title.lower():
            return book
        
    return None


def find_book_by_title_and_author(books, title, author):

    for book in books:
        if (
            book.title.lower() == title.lower()
            and
            book.author.lower() == author.lower()
        ):
            return book
        
    return None
