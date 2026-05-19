import helpers

class Book:

    def __init__(self, book_id, title, author):
        self.id = book_id
        self.title = title
        self.author = author
        self.available = True


    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "available": self.available
        }


    def __str__(self):
        status = "available" if self.available else "borrowed"
        return f"{self.id} | {self.title} | {self.author} | {status}"
    

class User:

    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name
        self.borrowed_books = []


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "borrowed_books": [
                book.id for book in self.borrowed_books
            ]
        }


    def borrow_book(self, book):

        if not book.available:
            print("book already borrowed!")
            return False
        
        self.borrowed_books.append(book)

        book.available = False

        print("book borrowed!")

        return True


    def show_books(self):

        if not self.borrowed_books:
            print("no borrowed books!")
            return
        
        for book in self.borrowed_books:
            print(book)


    def return_book(self, book):
        
        if book not in self.borrowed_books:
            print(f"this book was not borrowed by {self.name}")
            return False
        
        self.borrowed_books.remove(book)

        book.available = True

        print("book returned!")

        return True


    def __str__(self):
        return f"{self.id} | {self.name}"
    

class Library:

    def __init__(self):
        self.books = []
        self.users = []

        self.next_book_id = 1
        self.next_user_id = 1


    # core methods
   
    def add_book(self):

        while True:

            title = input("title book (q to cancel): ").strip()
            if title.lower() == "q":
                print("operation cancelled!")
                return
            
            author = input("author name: ").strip()

            if not title or not author:
                print("title's and author's fields are required!")
                continue
        
            existing_book = helpers.find_book_by_title_and_author(self.books, title, author)

            if existing_book:
                print(f"{existing_book.title} already exists!")
                continue

            new_book = Book(self.next_book_id, title, author)
            self.books.append(new_book)
            self.next_book_id += 1

            print(f"{new_book.title} book added successfully!")
            break


    def show_books(self):

        if not self.books:
            print("no book found!")
            return
        
        for book in self.books:
            print(book)


    def search_book(self):

        while True:

            title = input("enter book title or (q to cancel): ").strip()
            if title.lower() == "q":
                print("operation cancelled!")
                return

            if not title:
                print("please enter a book title!")
                continue
        
            found_book = helpers.find_book_by_title(self.books, title)

            if not found_book:
                print("no book found!")
                continue
        
            print("\nbook found:")
            print(found_book)

            break


    def delete_book(self):

        while True:

            title = input("enter book title to delete or (q to cancel): ").strip()
            if title.lower() == "q":
                print("operation cancelled!")
                return

            if not title:                
                print("please enter a book title!")
                continue
        
            found_book = helpers.find_book_by_title(self.books, title)

            if not found_book:
                print("no book found!")
                continue
        
            if not found_book.available:
                print("cant delete borrowed books!")
                continue
        
            self.books.remove(found_book)

            print(f"{found_book.title} deleted successfully!")
            break


    def add_user(self):

        while True:

            name = input("user name (q to cancel): ").strip()
            if name.lower() == "q":
                print("operation cancelled!")
                return

            if not name:
                print("this field is required!")
                continue
        
            existing_name = helpers.find_user_by_name(self.users, name)

            if existing_name:
                print("this name already exists!")
                continue
        
            new_user = User(self.next_user_id, name)        
            self.users.append(new_user)
            self.next_user_id += 1

            print(f"{new_user.name} added successfully!")
            break


    def show_users(self):

        if not self.users:
            print("no user found!")
            return
        
        for user in self.users:
            print(user)


    def search_user(self):

        while True:

            name = input("enter user name or (q to cancel): ").strip()

            if name.lower() == "q":
                print("operation cancelled!")
                return

            if not name:
                print("please enter a user name!")
                continue
        
            found_user = helpers.find_user_by_name(self.users, name)

            if not found_user:
                print("no user found!")
                continue
        
            print("\nuser found:")
            print(found_user)
            print(f"borrowed books:{len(found_user.borrowed_books)}")

            break


    def delete_user(self):

        while True:

            name = input("enter user name to delete or (q to cancel): ").strip()

            if name.lower() == "q":
                print("operation cancelled")
                return

            if not name:
                print("please enter a user name!")
                continue
        
            found_user = helpers.find_user_by_name(self.users, name)

            if not found_user:
                print("no user found!")
                continue
        
            if found_user.borrowed_books:
                print("cant delete user with borrowed books!")
                continue
        
            self.users.remove(found_user)

            print(f"{found_user.name} deleted successfully!")
            break


    def borrow_book_to(self):

        while True:

            name = input("enter user name or (q to cancel): ").strip()

            if name.lower() == "q":
                print("operation cancelled!")
                return
            
            title = input("enter title book: ").strip()

            if not name or not title:
                print("user name's and book title's fields are required!")
                continue
        
            found_user = helpers.find_user_by_name(self.users, name)
            found_book = helpers.find_book_by_title(self.books, title)

            if not found_user:
                print("no user found!")
                continue
        
            if not found_book:
                print("no book found!")
                continue

            success = found_user.borrow_book(found_book)

            if success:
                break
        

    def show_user_books(self):
    
        name = input("enter user's name: ").strip()

        if not name:
            print("please enter a user name!")
            return
    
        found_user = helpers.find_user_by_name(self.users, name)

        if not found_user:
            print("no user found!")
            return
        
        print(f"\n{found_user.name} borrowed books:")
        found_user.show_books()


    def return_book_from(self):

        while True:

            name = input("enter user name or (q to cancel): ").strip()

            if name.lower() == "q":
                print("operation cancelled!")
                return
            
            title = input("enter book title: ").strip()

            if not name or not title:
                print("user name's and book title's fields are required!")
                continue
        
            found_user = helpers.find_user_by_name(self.users, name)
            found_book = helpers.find_book_by_title(self.books, title)

            if not found_user:
                print("no user found!")
                continue
        
            if not found_book:
                print("no book found!")
                continue
        
            success = found_user.return_book(found_book)

            if success:
                break


    def __str__(self):
        return f"library | books: {len(self.books)} | users: {len(self.users)}"

