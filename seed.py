from faker import Faker
from sqlalchemy.orm import Session
from database import SessionLocal, init_db
from models import Book, Author, BookCopy, User, BorrowRecord

# Initialize Faker
fake = Faker()

# Initialize database
init_db()
session = SessionLocal()

def seed_authors(num_authors=10):
    """Seed authors with fake names."""
    for _ in range(num_authors):
        author = Author(name=fake.name())
        session.add(author)
    session.commit()
    print(f"Seeded {num_authors} authors.")

def seed_books(num_books=20):
    """Seed books with fake titles and genres."""
    authors = session.query(Author).all()
    if not authors:
        print("No authors found. Please seed authors first.")
        return
    
    for _ in range(num_books):
        book = Book(
            title=fake.catch_phrase(),
            genre=fake.word(),
            authors=fake.random_elements(elements=authors, length=fake.random_int(min=1, max=3),  # Assign 1-3 random authors
        )
        session.add(book)
    session.commit()
    print(f"Seeded {num_books} books.")

def seed_book_copies(num_copies=50):
    """Seed book copies for existing books."""
    books = session.query(Book).all()
    if not books:
        print("No books found. Please seed books first.")
        return
    
    for _ in range(num_copies):
        book = fake.random_element(elements=books)
        book_copy = BookCopy(book_id=book.id)
        session.add(book_copy)
    session.commit()
    print(f"Seeded {num_copies} book copies.")

def seed_users(num_users=10):
    """Seed users with fake names."""
    for _ in range(num_users):
        user = User(name=fake.name())
        session.add(user)
    session.commit()
    print(f"Seeded {num_users} users.")

def seed_borrow_records(num_records=30):
    """Seed borrow records for users and book copies."""
    users = session.query(User).all()
    book_copies = session.query(BookCopy).all()
    
    if not users or not book_copies:
        print("No users or book copies found. Please seed users and book copies first.")
        return
    
    for _ in range(num_records):
        user = fake.random_element(elements=users)
        book_copy = fake.random_element(elements=book_copies)
        
        # Ensure the book copy is available
        if book_copy.status == "available":
            book_copy.status = "borrowed"
            borrow_record = BorrowRecord(user_id=user.id, book_copy_id=book_copy.id)
            session.add(borrow_record)
    session.commit()
    print(f"Seeded {num_records} borrow records.")

def main():
    """Seed the database with fake data."""
    seed_authors()
    seed_books()
    seed_book_copies()
    seed_users()
    seed_borrow_records()
    print("Database seeding completed!")

if __name__ == "__main__":
    main()