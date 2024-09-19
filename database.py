import psycopg2

def connect():
    """Establish a connection to the PostgreSQL database."""
    return psycopg2.connect(
        dbname="tracker",     # The name of the database
        user="honey",         # The database user
        password="nash",      # The password for the user
        host="localhost"      # The host where the database is running (localhost for local development)
    )

def create_tables():
    """Create tables for symptoms, conditions, and their relationship."""
    try:
        # Connect to the database and obtain a cursor for executing SQL queries
        with connect() as conn:
            with conn.cursor() as cursor:
                # Creating the 'symptoms' table to store symptom data
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS symptoms (
                        id SERIAL PRIMARY KEY,           # Unique ID for each symptom, auto-incrementing
                        name VARCHAR(255) NOT NULL,      # Name of the symptom, required field
                        severity INT NOT NULL,           # Severity level (integer), required field
                        date DATE NOT NULL,              # Date when the symptom occurred, required field
                        notes TEXT                       # Optional notes for additional details
                    );
                ''')

                # Creating the 'conditions' table to store medical condition data
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS conditions (
                        id SERIAL PRIMARY KEY,           # Unique ID for each condition, auto-incrementing
                        name VARCHAR(255) NOT NULL,      # Name of the condition, required field
                        description TEXT                 # Description of the condition, optional
                    );
                ''')

                # Creating the 'symptom_condition' table for a many-to-many relationship
                # between 'symptoms' and 'conditions' (linking symptoms to conditions)
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS symptom_condition (
                        symptom_id INT REFERENCES symptoms(id),    # Foreign key referencing the 'symptoms' table
                        condition_id INT REFERENCES conditions(id), # Foreign key referencing the 'conditions' table
                        PRIMARY KEY (symptom_id, condition_id)      # Composite primary key to prevent duplicate entries
                    );
                ''')

                # Commit the transaction to save the changes to the database
                conn.commit()
    except Exception as e:
        # Catch and print any errors that occur during the table creation process
        print(f"An error occurred while creating tables: {e}")

# If the script is run directly, this block will execute, creating the tables
if __name__ == "__main__":
    create_tables
