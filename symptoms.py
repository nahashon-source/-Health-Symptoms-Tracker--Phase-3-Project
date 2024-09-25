# import os
# import logging
# import psycopg2
# from database import connect

# # Configure logging
# logging.basicConfig(level=logging.INFO)

# def validate_symptom(name, severity, date, notes):
#     if not name or not isinstance(name, str):
#         raise ValueError("Symptom name must be a non-empty string.")
#     if not (1 <= severity <= 10):
#         raise ValueError("Severity must be between 1 and 10.")
#     if not isinstance(date, str):
#         raise ValueError("Date must be a string in YYYY-MM-DD format.")
#     if notes and not isinstance(notes, str):
#         raise ValueError("Notes must be a string if provided.")

# def add_symptom(name, severity, date, notes=""):
#     """Add a new symptom to the database."""
#     validate_symptom(name, severity, date, notes)
#     try:
#         with connect() as conn:
#             with conn.cursor() as cursor:
#                 cursor.execute('''
#                     INSERT INTO symptoms (name, severity, date, notes)
#                     VALUES (%s, %s, %s, %s);
#                 ''', (name, severity, date, notes))
#                 conn.commit()
#                 logging.info("Symptom added successfully!")
#                 return True
#     except ValueError as ve:
#         logging.error(f"Invalid input: {ve}")
#         return False
#     except Exception as e:
#         logging.error(f"An error occurred while adding the symptom: {e}")
#         return False

# def view_symptoms():
#     """Retrieve all symptoms from the database."""
#     try:
#         with connect() as conn:
#             with conn.cursor() as cursor:
#                 cursor.execute('SELECT * FROM symptoms;')
#                 return cursor.fetchall()
#     except Exception as e:
#         logging.error(f"An error occurred while retrieving symptoms: {e}")
#         return []

# def delete_symptom(symptom_id):
#     """Delete a symptom by ID."""
#     try:
#         with connect() as conn:
#             with conn.cursor() as cursor:
#                 cursor.execute('DELETE FROM symptoms WHERE id = %s;', (symptom_id,))
#                 conn.commit()
#                 logging.info("Symptom deleted successfully!")
#                 return True
#     except Exception as e:
#         logging.error(f"An error occurred while deleting the symptom: {e}")
#         return False

# def update_symptom(symptom_id, name, severity, date, notes=""):
#     """Update an existing symptom's details."""
#     validate_symptom(name, severity, date, notes)
#     try:
#         with connect() as conn:
#             with conn.cursor() as cursor:
#                 cursor.execute('''
#                     UPDATE symptoms
#                     SET name = %s, severity = %s, date = %s, notes = %s
#                     WHERE id = %s;
#                 ''', (name, severity, date, notes, symptom_id))
#                 conn.commit()
#                 logging.info("Symptom updated successfully!")
#                 return True
#     except Exception as e:
#         logging.error(f"An error occurred while updating the symptom: {e}")
#         return False

# # Test section
# if __name__ == "__main__":
#     # Example usage
#     add_symptom("Headache", 5, "2024-09-20", "Mild headache.")
#     symptoms = view_symptoms()
#     print(symptoms)

# symptoms.py

from database import connect
import logging
from datetime import datetime

def validate_severity(severity):
    """Ensures that the severity is between 1 and 10."""
    try:
        severity = int(severity)
        if severity < 1 or severity > 10:
            raise ValueError("Severity must be between 1 and 10.")
        return severity
    except ValueError as e:
        print(e)
        return None

def validate_date(date_str):
    """Validates the date format (YYYY-MM-DD)."""
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return False

def add_symptom(name, severity, date, notes):
    """Add a new symptom to the database."""
    if not name:
        print("Symptom name cannot be empty.")
        return
    try:
        severity = validate_severity(severity)
        if severity is None or not validate_date(date):
            return
        
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute('''
                    INSERT INTO symptoms (name, severity, date, notes)
                    VALUES (%s, %s, %s, %s);
                ''', (name, severity, date, notes))
                conn.commit()
                logging.info(f"Added symptom: {name}")
                print("Symptom added successfully!")
    except Exception as e:
        logging.error(f"Error adding symptom: {e}")
        print("An error occurred while adding the symptom.")

def view_symptoms():
    """Retrieve all symptoms from the database."""
    try:
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT * FROM symptoms;')
                return cursor.fetchall()
    except Exception as e:
        logging.error(f"Error retrieving symptoms: {e}")
        print("An error occurred while retrieving symptoms.")
        return []

def search_symptoms(keyword):
    """Search for symptoms by name."""
    try:
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute('''
                    SELECT * FROM symptoms
                    WHERE name ILIKE %s;
                ''', (f'%{keyword}%',))
                return cursor.fetchall()
    except Exception as e:
        logging.error(f"Error searching for symptoms: {e}")
        print("An error occurred while searching for symptoms.")
        return []

def delete_symptom(symptom_id):
    """Delete a symptom by ID."""
    try:
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute('DELETE FROM symptoms WHERE id = %s;', (symptom_id,))
                conn.commit()
                logging.info(f"Deleted symptom with ID: {symptom_id}")
                print("Symptom deleted successfully!")
    except Exception as e:
        logging.error(f"Error deleting symptom: {e}")
        print("An error occurred while deleting the symptom.")

def update_symptom(symptom_id, name, severity, date, notes):
    """Update an existing symptom's details."""
    if not name:
        print("Symptom name cannot be empty.")
        return
    try:
        severity = validate_severity(severity)
        if severity is None or not validate_date(date):
            return
            
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute('''
                    UPDATE symptoms
                    SET name = %s, severity = %s, date = %s, notes = %s
                    WHERE id = %s;
                ''', (name, severity, date, notes, symptom_id))
                conn.commit()
                logging.info(f"Updated symptom ID: {symptom_id}")
                print("Symptom updated successfully!")
    except Exception as e:
        logging.error(f"Error updating symptom: {e}")
        print("An error occurred while updating the symptom.")

