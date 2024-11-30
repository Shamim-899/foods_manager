from view_all_books import view_all_books
from save_all_books import save_all_books


def remove_book(all_books):
    view_all_books(all_books)

    book_index = int(input("Enter the number of the book to delete: ")) - 1


    if 0 <= book_index < len(all_books):
        book = all_books.pop(book_index)
        print(f"Book '{book['title']}' by {book['author']} has been deleted.")


        try:
            book['isbn'] = int(book['isbn'])
            book['price'] = int(book['price'])
            book['quantity'] = int(book['quantity'])
        except ValueError:
            print("Invalid input for ISBN, price, or quantity. Please enter valid integers.")
            return


        save_all_books(all_books)
    else:
        print("Invalid selection. Please try again.")
