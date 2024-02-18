class Library:
    # Constructor Fonksiyonu
    def __init__(self):
        self.file = open("../Python_Final_Project/books.txt", "a+", encoding='utf-8')

    # Destructor Fonksiyonu
    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0) 
        books = self.file.readlines()
        if not books:
            print("No books found. \n")
        else:
            for book in books:
                book_info = book.strip().split(",")
                print(f"- Title: {book_info[0]}, Author: {book_info[1]}, Release Year: {book_info[2]}, Number of Pages: {book_info[3]} \n")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")

        try:
            release_year = int(input("Enter release year: "))
            num_pages = int(input("Enter number of pages: "))
        except ValueError:
            print(" ")
            print("You must input a number! \n")
            return
        # Satır satır olacak şekilde kitap bilgisini ekle
        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully. \n")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        books = self.file.readlines()
        new_books = []
        removed = False
        for book in books:
            book_info = book.strip().split(",")
            if book_info[0] != title_to_remove:
                new_books.append(book)
            else:
                removed = True
        if removed:
            self.file.seek(0)
            # Bu şekilde dosyanın içeriğini silmiş oluruz
            self.file.truncate()  
            self.file.writelines(new_books)
            print(f"Book '{title_to_remove}' removed successfully. \n")
        else:
            print(f"Book '{title_to_remove}' not found. \n")


lib = Library()


while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit \n")
    

    choice = input("Enter your choice (1-4): ")
    print(" ")
    
    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4. \n")

