import sys
from sqlalchemy.orm import Session
from models import Book, Author, BookCopy, User, BorrowRecord
from database import SessionLocal, init_db
from datetime import datetime

def add_book(session: Session, title: str, genre: str, author_names: list):
    authors = []
    for name in author_names:
        author = session.query(Author).filter(Author.name == name).first()
        if not author:
            author = Author(name=name)
            session.add(author)
        authors.append(author)
    
    book = Book(title=title, genre=genre, authors=authors)
    session.add(book)
    session.commit()
    print(f"Added book: {title}")

def list_books(session: Session):
    books = session.query(Book).all()
    for book in books:
        print(book)

def add_author(session: Session, name: str):
    author = Author(name=name)
    session.add(author)
    session.commit()
    print(f"Added author: {name}")

def list_authors(session: Session):
    authors = session.query(Author).all()
    for author in authors:
        print(author)

def add_book_copy(session: Session, book_id: int):
    book = session.query(Book).filter(Book.id == book_id).first()
    if not book:
        print("Book not found!")
        return
    
    book_copy = BookCopy(book_id=book_id)
    session.add(book_copy)
    session.commit()
    print(f"Added copy for book ID: {book_id}")

def list_book_copies(session: Session):
    copies = session.query(BookCopy).all()
    for copy in copies:
        print(copy)

def add_user(session: Session, name: str):
    user = User(name=name)
    session.add(user)
    session.commit()
    print(f"Added user: {name}")

def list_users(session: Session):
    users = session.query(User).all()
    for user in users:
        print(user)

def borrow_book(session: Session, user_id: int, book_copy_id: int):
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        print("User not found!")
        return
    
    book_copy = session.query(BookCopy).filter(BookCopy.id == book_copy_id).first()
    if not book_copy:
        print("Book copy not found!")
        return
    
    if book_copy.status != "available":
        print("Book copy is not available!")
        return
    
    book_copy.status = "borrowed"
    borrow_record = BorrowRecord(user_id=user_id, book_copy_id=book_copy_id)
    session.add(borrow_record)
    session.commit()
    print(f"User {user.name} borrowed book copy ID {book_copy_id}")

def return_book(session: Session, book_copy_id: int):
    book_copy = session.query(BookCopy).filter(BookCopy.id == book_copy_id).first()
    if not book_copy:
        print("Book copy not found!")
        return
    
    if book_copy.status != "borrowed":
        print("Book copy is not borrowed!")
        return
    
    borrow_record = session.query(BorrowRecord).filter(BorrowRecord.book_copy_id == book_copy_id, BorrowRecord.return_date == None).first()
    if not borrow_record:
        print("No active borrow record found!")
        return
    
    borrow_record.return_date = datetime.utcnow()
    book_copy.status = "available"
    session.commit()
    print(f"Book copy ID {book_copy_id} returned")

def list_borrow_records(session: Session):
    records = session.query(BorrowRecord).all()
    for record in records:
        print(record)

def main():
    init_db()
    session = SessionLocal()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. List Books")
        print("3. Add Author")
        print("4. List Authors")
        print("5. Add Book Copy")
        print("6. List Book Copies")
        print("7. Add User")
        print("8. List Users")
        print("9. Borrow Book")
        print("10. Return Book")
        print("11. List Borrow Records")
        print("12. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            title = input("Enter book title: ")
            genre = input("Enter book genre: ")
            authors = input("Enter author names (comma separated): ").split(",")
            add_book(session, title, genre, authors)
        
        elif choice == "2":
            list_books(session)
        
        elif choice == "3":
            name = input("Enter author name: ")
            add_author(session, name)
        
        elif choice == "4":
            list_authors(session)
        
        elif choice == "5":
            book_id = int(input("Enter book ID: "))
            add_book_copy(session, book_id)
        
        elif choice == "6":
            list_book_copies(session)
        
        elif choice == "7":
            name = input("Enter user name: ")
            add_user(session, name)
        
        elif choice == "8":
            list_users(session)
        
        elif choice == "9":
            user_id = int(input("Enter user ID: "))
            book_copy_id = int(input("Enter book copy ID: "))
            borrow_book(session, user_id, book_copy_id)
        
        elif choice == "10":
            book_copy_id = int(input("Enter book copy ID: "))
            return_book(session, book_copy_id)
        
        elif choice == "11":
            list_borrow_records(session)
        
        elif choice == "12":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
