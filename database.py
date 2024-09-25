# import psycopg2
# from psycopg2 import OperationalError

# def connect():
#     """Establish a connection to the PostgreSQL database."""
#     try:
#         connection = psycopg2.connect(
#             dbname="tracker",     # Replace with your database name
#             user="honey",         # Replace with your database user
#             password="nash",      # Replace with your database password
#             host="localhost"      # The host where the database is running
#         )
#         print("Connection to the database established successfully.")
#         return connection
#     except OperationalError as e:
#         print(f"The error '{e}' occurred while connecting to the database.")
#         return None

# def create_tables():
#     """Create tables for symptoms, conditions, and their relationship."""
#     try:
#         with connect() as conn:
#             with conn.cursor() as cursor:
#                 cursor.execute('''
#                     CREATE TABLE IF NOT EXISTS symptoms (
#                         id SERIAL PRIMARY KEY,
#                         name VARCHAR(255) NOT NULL,
#                         severity INT CHECK (severity >= 1 AND severity <= 10) NOT NULL,
#                         date DATE NOT NULL,
#                         notes TEXT
#                     );
#                 ''')

#                 cursor.execute('''
#                     CREATE TABLE IF NOT EXISTS conditions (
#                         id SERIAL PRIMARY KEY,
#                         name VARCHAR(255) NOT NULL,
#                         description TEXT
#                     );
#                 ''')

#                 cursor.execute('''
#                     CREATE TABLE IF NOT EXISTS symptom_condition (
#                         symptom_id INT REFERENCES symptoms(id) ON DELETE CASCADE,
#                         condition_id INT REFERENCES conditions(id) ON DELETE CASCADE,
#                         PRIMARY KEY (symptom_id, condition_id)
#                     );
#                 ''')

#                 conn.commit()
#     except Exception as e:
#         print(f"An error occurred while creating tables: {e}")

# if __name__ == "__main__":
#     create_tables()

# database.py

import psycopg2
import logging

# Configure logging
logging.basicConfig(filename='tracker.log', level=logging.INFO)

def connect():
    """Establish a connection to the PostgreSQL database."""
    try:
        return psycopg2.connect(
            dbname="tracker",  # Replace with your database name
            user="honey",      # Replace with your database user
            password="nash",   # Replace with your database password
            host="localhost"   # The host where the database is running
        )
    except Exception as e:
        logging.error(f"Error connecting to database: {e}")
        print("Failed to connect to the database.")
