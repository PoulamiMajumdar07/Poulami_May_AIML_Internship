def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)


def borrow_book(catalog, borrowed_books, book_id):

    if book_id in catalog:

        if book_id not in borrowed_books:
            borrowed_books.append(book_id)
            print(f"Book {book_id} borrowed successfully")

        else:
            print("Book already borrowed")

    else:
        print("Book does not exist")


def return_book(borrowed_books, book_id):

    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Book {book_id} returned")

    else:
        print("Book was not borrowed")


def register_member(members, member_id):
    members.add(member_id)


def show_available(catalog, borrowed_books):

    print("\nAvailable Books:")

    for book_id, details in catalog.items():

        if book_id not in borrowed_books:

            title, author, year = details

            print(f"{book_id} -> {title} by {author} ({year})")


def main():

    catalog = {}
    borrowed_books = []
    members = set()

    add_book(catalog, 1, "Python Basics", "John Smith", 2020)
    add_book(catalog, 2, "Data Structures", "Alice Brown", 2019)
    add_book(catalog, 3, "Machine Learning", "David Lee", 2021)
    add_book(catalog, 4, "Cyber Security", "Emma Wilson", 2022)

   
    register_member(members, 101)
    register_member(members, 102)
    register_member(members, 103)

   
    register_member(members, 101)

    print("Members:", members)

    borrow_book(catalog, borrowed_books, 1)
    borrow_book(catalog, borrowed_books, 2)

    return_book(borrowed_books, 1)

    show_available(catalog, borrowed_books)


main()

