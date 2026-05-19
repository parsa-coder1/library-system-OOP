from models import Library

from storage import save_data, load_data

def main():

    library = Library()

    load_data(library)

    while True:
        print("\n=== library system ===")
        print("1. add book")
        print("2. show books")
        print("3. search book")
        print("4. delete book")
        print("5. add user")
        print("6. show users")
        print("7. search user")
        print("8. delete user")
        print("9. borrow book")
        print("10. show user's books")
        print("11. return book")
        print("12. exit")

        choice = input("choose: ").strip()

        if choice == "1":
            library.add_book()
            save_data(library)

        elif choice == "2":
            library.show_books()

        elif choice == "3":
            library.search_book()

        elif choice == "4":
            library.delete_book()
            save_data(library)

        elif choice == "5":
            library.add_user()
            save_data(library)

        elif choice == "6":
            library.show_users()

        elif choice == "7":
            library.search_user()

        elif choice == "8":
            library.delete_user()
            save_data(library)

        elif choice == "9":
            library.borrow_book_to()
            save_data(library)

        elif choice == "10":
            library.show_user_books()

        elif choice == "11":
            library.return_book_from()
            save_data(library)

        elif choice == "12":
            save_data(library)
            print("exited from system!")
            break

        else:
            print("invalid choice!")

if __name__ == "__main__":
    main()
