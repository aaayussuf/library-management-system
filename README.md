# library-management-system

A command-line application to manage library books, users, and borrowing records using Python, SQLAlchemy, Alembic and CLI.

## Features
- User Management: Add and list users.
- Book Management: Add books, list books, and track copies.
- Borrowing System: Borrow and return books.
- Database Integration: Uses SQLite with SQLAlchemy ORM.
- Migrations: Supports database migrations using Alembic.
- Data Seeding: Populates the database with sample data using Faker.

## Project structure
library-management-system/
── alembic/               # Alembic migrations directory
── database.py            # Database connection setup
── models.py              # SQLAlchemy ORM models
── cli.py                 # Command-line interface
── main.py                # Entry point
── seed.py                # Script to populate sample data
── README.md              # Documentation
── library.db             # SQLite database file (after running)

## Installation & Setup
pipenv install
pipenv shell
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
python3 main.py

## Futures inhancement
Search functionality for books and users.
Due date tracking for borrowed books.
Admin authentication for restricted actions.
Detailed Reports for book availability and borrowing history.

## Clone the Repository**
```sh
git clone https://github.com/aaayussuf/library-management-system.git

