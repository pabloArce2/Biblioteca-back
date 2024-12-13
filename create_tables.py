from app.database import Base, engine
from app.models.general import User
from app.models.general import Book
from app.models.general import Library
from app.models.general import Loan

def create_tables():
    try:
        print("Starting table creation process...")
        print("Models registered:", Base.metadata.tables.keys())  # Imprime las tablas registradas
        
        print("Dropping all tables...")
        Base.metadata.drop_all(bind=engine)
        
        print("Creating all tables...")
        Base.metadata.create_all(bind=engine)
        
        print("Tables created successfully!")
        # Imprime las tablas creadas para verificar
        print("Created tables:", engine.table_names())
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    create_tables() 