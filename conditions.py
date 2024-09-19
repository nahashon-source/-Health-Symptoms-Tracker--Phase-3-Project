from database import connect

def add_condition(name, description):
    """Add a new condition to the database."""
    print(f"Adding condition: {name}, {description}")  # Log the condition being added
    try:
        # Establish database connection and cursor
        with connect() as conn:
            with conn.cursor() as cursor:
                # Insert the new condition into the 'conditions' table
                cursor.execute('''
                    INSERT INTO conditions (name, description)
                    VALUES (%s, %s);
                ''', (name, description))
                # Commit the transaction to save changes
                conn.commit()
                print("Condition added successfully!")
    except Exception as e:
        # Catch and log any errors that occur during the database operation
        print(f"An error occurred while adding the condition: {e}")

def view_conditions():
    """Retrieve all conditions from the database."""
    # Establish database connection and cursor
    with connect() as conn:
        with conn.cursor() as cursor:
            # Select all records from the 'conditions' table
            cursor.execute('SELECT * FROM conditions;')
            # Fetch and return all rows from the result
            return cursor.fetchall()

def delete_condition(condition_id):
    """Delete a condition by ID."""
    # Establish database connection and cursor
    with connect() as conn:
        with conn.cursor() as cursor:
            # Delete the condition with the matching ID
            cursor.execute('DELETE FROM conditions WHERE id = %s;', (condition_id,))
            # Commit the transaction to save changes
            conn.commit()

def update_condition(condition_id, name, description):
    """Update an existing condition's name and description."""
    # Establish database connection and cursor
    with connect() as conn:
        with conn.cursor() as cursor:
            # Update the name and description of the condition with the given ID
            cursor.execute('''
                UPDATE conditions
                SET name = %s, description = %s
                WHERE id = %s;
            ''', (name, description, condition_id))
            # Commit the transaction to save changes
            conn.commit()
