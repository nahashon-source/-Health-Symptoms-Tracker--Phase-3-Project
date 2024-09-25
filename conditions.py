# import os
# import logging
# import psycopg2
# from database import connect

# # Configure logging
# logging.basicConfig(level=logging.INFO)

# def validate_condition(name, description):
#     if not name or not isinstance(name, str):
#         raise ValueError("Condition name must be a non-empty string.")
#     if description and not isinstance(description, str):
#         raise ValueError("Description must be a string if provided.")

# def add_condition(name, description):
#     validate_condition(name, description)
#     logging.info(f"Adding condition: {name}, {description}")
#     try:
#         with connect() as conn:
#             with conn.cursor() as cursor:
#                 cursor.execute('''
#                     INSERT INTO conditions (name, description)
#                     VALUES (%s, %s);
#                 ''', (name, description))
#                 conn.commit()
#                 logging.info("Condition added successfully!")
#                 return True
#     except Exception as e:
#         logging.error(f"An error occurred while adding the condition: {e}")
#         return False

# def view_conditions():
#     """Retrieve all conditions from the database."""
#     try:
#         with connect() as conn:
#             with conn.cursor() as cursor:
#                 cursor.execute('SELECT * FROM conditions;')
#                 return cursor.fetchall()
#     except Exception as e:
#         logging.error(f"An error occurred while retrieving conditions: {e}")
#         return []

# def delete_condition(condition_id):
#     """Delete a condition by ID."""
#     try:
#         with connect() as conn:
#             with conn.cursor() as cursor:
#                 cursor.execute('DELETE FROM conditions WHERE id = %s;', (condition_id,))
#                 conn.commit()
#                 logging.info("Condition deleted successfully!")
#                 return True
#     except Exception as e:
#         logging.error(f"An error occurred while deleting the condition: {e}")
#         return False

# def update_condition(condition_id, name, description):
#     validate_condition(name, description)
#     try:
#         with connect() as conn:
#             with conn.cursor() as cursor:
#                 cursor.execute('''
#                     UPDATE conditions
#                     SET name = %s, description = %s
#                     WHERE id = %s;
#                 ''', (name, description, condition_id))
#                 conn.commit()
#                 logging.info("Condition updated successfully!")
#                 return True
#     except Exception as e:
#         logging.error(f"An error occurred while updating the condition: {e}")
#         return False

# # Test section
# if __name__ == "__main__":
#     # Example usage
#     add_condition("Example Condition", "This is an example condition description.")
#     conditions = view_conditions()
#     print(conditions)


# conditions.py

from database import connect
import logging

def add_condition(name, description):
    """Add a new condition to the database."""
    if not name:
        print("Condition name cannot be empty.")
        return
    try:
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute('''
                    INSERT INTO conditions (name, description)
                    VALUES (%s, %s);
                ''', (name, description))
                conn.commit()
                logging.info(f"Added condition: {name}")
                print("Condition added successfully!")
    except Exception as e:
        logging.error(f"Error adding condition: {e}")
        print("An error occurred while adding the condition.")

def view_conditions():
    """Retrieve all conditions from the database."""
    try:
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT * FROM conditions;')
                return cursor.fetchall()
    except Exception as e:
        logging.error(f"Error retrieving conditions: {e}")
        print("An error occurred while retrieving conditions.")
        return []

def delete_condition(condition_id):
    """Delete a condition by ID."""
    try:
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute('DELETE FROM conditions WHERE id = %s;', (condition_id,))
                conn.commit()
                logging.info(f"Deleted condition with ID: {condition_id}")
                print("Condition deleted successfully!")
    except Exception as e:
        logging.error(f"Error deleting condition: {e}")
        print("An error occurred while deleting the condition.")

def update_condition(condition_id, name, description):
    """Update an existing condition's details."""
    if not name:
        print("Condition name cannot be empty.")
        return
    try:
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute('''
                    UPDATE conditions
                    SET name = %s, description = %s
                    WHERE id = %s;
                ''', (name, description, condition_id))
                conn.commit()
                logging.info(f"Updated condition ID: {condition_id}")
                print("Condition updated successfully!")
    except Exception as e:
        logging.error(f"Error updating condition: {e}")
        print("An error occurred while updating the condition.")
