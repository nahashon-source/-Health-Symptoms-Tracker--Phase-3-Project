from database import connect

def add_symptom(name, severity, date, notes=""):
    """Add a new symptom to the database."""
    try:
        # Connect to the database and obtain a cursor for executing SQL queries
        with connect() as conn:
            with conn.cursor() as cursor:
                # Insert the new symptom into the 'symptoms' table
                cursor.execute('''
                    INSERT INTO symptoms (name, severity, date, notes)
                    VALUES (%s, %s, %s, %s);
                ''', (name, severity, date, notes))  # Ensure 'date' is in 'YYYY-MM-DD' format
                # Commit the transaction to save changes
                conn.commit()
                print("Symptom added successfully!")
    except ValueError as ve:
        # Handle incorrect date format errors
        print(f"Invalid date format: {ve}. Please use YYYY-MM-DD.")
    except Exception as e:
        # Catch any other exceptions that occur while adding the symptom
        print(f"An error occurred while adding the symptom: {e}")

def view_symptoms():
    """Retrieve all symptoms from the database."""
    try:
        # Connect to the database and obtain a cursor for executing SQL queries
        with connect() as conn:
            with conn.cursor() as cursor:
                # Select all records from the 'symptoms' table
                cursor.execute('SELECT * FROM symptoms;')
                # Fetch all rows from the result set and return them
                symptoms = cursor.fetchall()
                return symptoms
    except Exception as e:
        # Catch any errors that occur while retrieving symptoms
        print(f"An error occurred while retrieving symptoms: {e}")
        return []

def delete_symptom(symptom_id):
    """Delete a symptom by ID."""
    try:
        # Connect to the database and obtain a cursor for executing SQL queries
        with connect() as conn:
            with conn.cursor() as cursor:
                # Delete the symptom with the given ID
                cursor.execute('DELETE FROM symptoms WHERE id = %s;', (symptom_id,))
                # Commit the transaction to save changes
                conn.commit()
                print("Symptom deleted successfully!")
    except Exception as e:
        # Catch any errors that occur while deleting the symptom
        print(f"An error occurred while deleting the symptom: {e}")

def update_symptom(symptom_id, name, severity, date, notes=""):
    """Update an existing symptom's details."""
    try:
        # Connect to the database and obtain a cursor for executing SQL queries
        with connect() as conn:
            with conn.cursor() as cursor:
                # Update the symptom's details based on the provided data
                cursor.execute('''
                    UPDATE symptoms
                    SET name = %s, severity = %s, date = %s, notes = %s
                    WHERE id = %s;
                ''', (name, severity, date, notes, symptom_id))
                # Commit the transaction to save changes
                conn.commit()
                print("Symptom updated successfully!")
    except Exception as e:
        # Catch any errors that occur while updating the symptom
        print(f"An error occurred while updating the symptom: {e}")
