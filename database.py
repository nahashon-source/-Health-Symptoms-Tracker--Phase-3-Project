import psycopg2

def connect():
    """Establish a connection to the PostgreSQL database."""
    return psycopg2.connect(
        dbname="tracker",
        user="honey",
        password="nash",
        host="localhost"
    )

def create_tables():
    """Create tables for symptoms, conditions, and their relationship."""
    try:
        with connect() as conn:
            with conn.cursor() as cursor:
                # Creating the Symptoms table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS symptoms (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(255) NOT NULL,
                        severity INT NOT NULL,
                        date DATE NOT NULL,
                        notes TEXT
                    );
                ''')
                
                # Creating the Conditions table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS conditions (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(255) NOT NULL,
                        description TEXT
                    );
                ''')

                # Creating the Symptom_Condition table (Many-to-Many Relationship)
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS symptom_condition (
                        symptom_id INT REFERENCES symptoms(id),
                        condition_id INT REFERENCES conditions(id),
                        PRIMARY KEY (symptom_id, condition_id)
                    );
                ''')

                conn.commit()
    except Exception as e:
        print(f"An error occurred while creating tables: {e}")

if __name__ == "__main__":
    create_tables()
