class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author 
        self.is_available = True # initially when book is added to management system, its available in the library

    def checkout(self):
        if self.is_available: # checks if the book is there in the system, if its available you can borrow form the library
            self.is_available = False # once its borrowed now its not available in the library, so its set to false
            return True # one book is successfully borrowed, it gives feedback that the borrowing process has been successful, so return True
        else:
            return False # it returns false if borrowing of book is unsuccessful
        
    def checkin(self):
        if not self.is_available: #checks the book is not available 
            self.is_available = True #someone returned the book and it becomes availbale 
            return True #Book returing process is successful
        else:
            return False # book returning process is unsuccessful
        
    def __str__(self):
        return f"{self.title} by {self.author}" # its special method that is usually used for decorating the string represention of an object

class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
class Library:
    def __init__(self):
        self.books = {} # created empty dictionary to store books
        self.students = {} #created empty dictiory to store students
    
    def add_book(self, book):
        self.books[book.title] = book # new attribute defined called book

    def add_student(self, student):
        self.students[student.name] = student
    
    def borrow_book(self, student_name, book_title):
        if student_name in self.students and book_title in self.books: #checks if the book and stdent available in the dictrionary
            student  = self.students[student_name] # updating name of the student with student name
            book = self.books[book_title]
            if book.checkout(): #calling checkout method in book object to check out availibility of the book
                return f"The {student} has borrowed {book}"
            else:
                return f"The book titled {book} not available "
        else:
            return f"Student and book not available"
    def return_book(self, student_name, book_title):
        if student_name in self.students and book_title in self.books: #checks if the book and stdent available in the dictrionary
            student  = self.students[student_name] # updating name of the student with student name
            book = self.books[book_title]
            if book.checkin(): #calling checkout method in book object to check out availibility of the book
                return f"The {student} has returned {book}"
            else:
                return f"The book titled {book} available "
        else:
            return f"Student and book not available"
        
library = Library()

book1 = Book("I am old", "Jeewan")
book2 = Book("Rich Dad Poor Dad", "Robert Kawasaki")

student1 = Student("Dema")
student2 = Student("Pema")

library.add_book(book1)
library.add_book(book2)

library.add_student(student1)
library.add_student(student2)

print(library.borrow_book("Dema", "I am old"))
print(library.return_book("Dema", "I am old"))
print(library.borrow_book("Dema", "I am old"))

