class Library:
    def __init__(self, filename='books.txt'):
        # Open the file in append and read mode, which also creates the file if it doesn't exist
        self.file = open(filename, 'a+')

    def __del__(self):
        # Close the file when the instance is destroyed
        self.file.close()

    def list_books(self):
        # Move the cursor to the beginning of the file
        self.file.seek(0)
        # Read the contents of the file and split into lines
        books = self.file.read().splitlines()
        # Print book names and authors
        for book in books:
            name, author, release_date, num_pages = book.split(', ')
            print(f"Book: {name}, Author: {author}")
        
    def add_book(self):
        # Ask user input for book details
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_year = input("Enter first release year: ")
        num_pages = input("Enter number of pages: ")
        # Create a string with the book information
        book_info = f"{title}, {author}, {release_year}, {num_pages}\n"
        # Append this line to the file
        self.file.write(book_info)
        self.file.flush()

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")
        # Move the cursor to the beginning of the file
        self.file.seek(0)
        # Read the file contents into a list
        books = self.file.read().splitlines()
        # Find the book to remove
        books = [book for book in books if not book.startswith(title_to_remove + ",")]
        # Clear the file and rewrite the remaining books
        self.file.seek(0)
        self.file.truncate()
        for book in books:
            self.file.write(f"{book}\n")
        self.file.flush()

# Create an instance of Library
lib = Library()

# Menu system
while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("q) Exit \n")
    choice = input("Enter your choice: ")

    if choice == 'q':
        break
    elif choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    else:
        print("Invalid choice. Please try again.")