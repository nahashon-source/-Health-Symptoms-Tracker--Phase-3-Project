from database import connect

def add_condition(name, description):
    """Add a new condition to the database."""
    with connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                INSERT INTO conditions (name, description)
                VALUES (%s, %s);
            ''', (name, description))
            conn.commit()

def view_conditions():
    """Retrieve all conditions from the database."""
    with connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM conditions;')
            return cursor.fetchall()

def delete_condition(condition_id):
    """Delete a condition by ID."""
    with connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute('DELETE FROM conditions WHERE id = %s;', (condition_id,))
            conn.commit()

def update_condition(condition_id, name, description):
    """Update an existing condition's name and description."""
    with connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                UPDATE conditions
                SET name = %s, description = %s
                WHERE id = %s;
            ''', (name, description, condition_id))
            conn.commit()
