##Library Management System##

This code designs a library management system and performs three core functions: 
listing books
adding books
removing books

It uses a text file (books.txt) to store book information. 

###Library Class:### 
Defines a class for managing book information. This class creates, reads, updates, and closes a file for storing book details.

###Initialization Function (__init__):### 
This function opens a file with the given filename (default is books.txt) in append and read mode ('a+' mode), which also creates the file if it doesn't exist.

###Destructor Function (__del__):### 
Defines a destructor function that closes the open file when a Library instance is deleted.

###list_books Method:### 
Lists all books in the file. For each book, it prints the name of the book and the author.

###add_book Method:### 
Prompts the user for information necessary to add a new book (title, author, first release year, number of pages) and appends this information to the file.

###remove_book Method:### 
Asks the user for the title of the book to be removed, finds the corresponding record in the file and removes it. Then, it updates the file with the remaining book information.

###Menu System:### 
Includes a simple menu system that presents the user with options to list books, add a book, and remove a book. The user enters a number to select the desired operation. The program can be exited by entering 'q'.
