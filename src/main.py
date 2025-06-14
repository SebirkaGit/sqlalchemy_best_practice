from database import init_db

# Run this once to create the contacts table in your PostgreSQL DB
if __name__ == "__main__":
    init_db()
    print("Database initialized. Tables created (if they didn't exist).")
