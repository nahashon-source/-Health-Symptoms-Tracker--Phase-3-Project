from database import connect

def add_symptom(name, severity, date, notes=""):
    """Add a new symptom to the database."""
    try:
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute('''
                    INSERT INTO symptoms (name, severity, date, notes)
                    VALUES (%s, %s, %s, %s);
                ''', (name, severity, date, notes))  # Ensure 'date' is in 'YYYY-MM-DD' format
                conn.commit()
                print("Symptom added successfully!")
    except ValueError as ve:
        print(f"Invalid date format: {ve}. Please use YYYY-MM-DD.")
    except Exception as e:
        print(f"An error occurred while adding the symptom: {e}")


def view_symptoms():
    """Retrieve all symptoms from the database."""
    try:
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT * FROM symptoms;')
                symptoms = cursor.fetchall()
                return symptoms
    except Exception as e:
        print(f"An error occurred while retrieving symptoms: {e}")
        return []

def delete_symptom(symptom_id):
    """Delete a symptom by ID."""
    try:
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute('DELETE FROM symptoms WHERE id = %s;', (symptom_id,))
                conn.commit()
                print("Symptom deleted successfully!")
    except Exception as e:
        print(f"An error occurred while deleting the symptom: {e}")

def update_symptom(symptom_id, name, severity, date, notes=""):
    """Update an existing symptom's details."""
    try:
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute('''
                    UPDATE symptoms
                    SET name = %s, severity = %s, date = %s, notes = %s
                    WHERE id = %s;
                ''', (name, severity, date, notes, symptom_id))
                conn.commit()
                print("Symptom updated successfully!")
    except Exception as e:
        print(f"An error occurred while updating the symptom: {e}")
