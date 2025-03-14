from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///library.db"  # Change path if needed

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Define Base
Base = declarative_base()

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function to initialize the database
def init_db():
    """Initialize the database and create tables."""
    from models import Book, Author, BookCopy, User, BorrowRecord  # Ensure models are imported
    Base.metadata.create_all(bind=engine)
