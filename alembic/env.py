from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from database import Base, engine  # Ensure correct import path
from models import Book, Author, BookCopy, User, BorrowRecord  # Import models

# Alembic Config object
config = context.config

# Configure logging from .ini file
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Set metadata for Alembic
target_metadata = Base.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    context.configure(
        url="sqlite:///your_database.db",  # Change this if needed
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
