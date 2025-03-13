from sqlalchemy import Column, Integer, String, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

# Association table for many-to-many relationship between Book and Author
book_author = Table(
    'book_author', Base.metadata,
    Column('book_id', Integer, ForeignKey('books.id')),
    Column('author_id', Integer, ForeignKey('authors.id'))
)

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    genre = Column(String)
    authors = relationship("Author", secondary=book_author, back_populates="books")
    copies = relationship("BookCopy", back_populates="book")

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', genre='{self.genre}')>"

class Author(Base):
    __tablename__ = 'authors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    books = relationship("Book", secondary=book_author, back_populates="authors")

    def __repr__(self):
        return f"<Author(id={self.id}, name='{self.name}')>"

class BookCopy(Base):
    __tablename__ = 'book_copies'
    
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    book = relationship("Book", back_populates="copies")
    status = Column(String, default="available")  # e.g., "available", "borrowed"
    borrow_records = relationship("BorrowRecord", back_populates="book_copy")

    def __repr__(self):
        return f"<BookCopy(id={self.id}, book_id={self.book_id}, status='{self.status}')>"

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    borrow_records = relationship("BorrowRecord", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}')>"

class BorrowRecord(Base):
    __tablename__ = 'borrow_records'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    book_copy_id = Column(Integer, ForeignKey('book_copies.id'))
    borrow_date = Column(DateTime, default=datetime.utcnow)
    return_date = Column(DateTime, nullable=True)
    user = relationship("User", back_populates="borrow_records")
    book_copy = relationship("BookCopy", back_populates="borrow_records")

    def __repr__(self):
        return f"<BorrowRecord(id={self.id}, user_id={self.user_id}, book_copy_id={self.book_copy_id}, borrow_date={self.borrow_date}, return_date={self.return_date})>"