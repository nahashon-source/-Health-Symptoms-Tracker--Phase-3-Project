import csv
from symptoms import view_symptoms, add_symptom
from conditions import view_conditions, add_condition

def export_to_csv(filename):
    """Export symptoms and conditions to a CSV file."""
    try:
        symptoms = view_symptoms()
        conditions = view_conditions()
        
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Symptoms'])
            writer.writerow(['ID', 'Name', 'Severity', 'Date', 'Notes'])
            for symptom in symptoms:
                writer.writerow(symptom)

            writer.writerow([])
            writer.writerow(['Conditions'])
            writer.writerow(['ID', 'Name', 'Description'])
            for condition in conditions:
                writer.writerow(condition)

        print(f"Data exported to {filename} successfully!")
    except Exception as e:
        print(f"Error exporting to CSV: {e}")

def import_from_csv(filename):
    """Import symptoms and conditions from a CSV file."""
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            current_section = None  # To keep track of which section we are in
            
            for row in reader:
                if not row:  # Skip empty rows
                    continue
                if row[0] == 'Symptoms':
                    current_section = 'Symptoms'
                    next(reader)  # Skip header
                    continue
                elif row[0] == 'Conditions':
                    current_section = 'Conditions'
                    next(reader)  # Skip header
                    continue

                if current_section == 'Symptoms':
                    # Handle symptoms import
                    if len(row) < 5:  # Check if there are enough columns
                        print(f"Skipping invalid symptom row: {row}")
                        continue
                    try:
                        # Convert severity to integer
                        severity = int(row[2])
                        add_symptom(row[1], severity, row[3], row[4])
                    except ValueError as ve:
                        print(f"Invalid severity for symptom {row[1]}: {ve}")
                elif current_section == 'Conditions':
                    # Handle conditions import
                    if len(row) < 3:  # Check if there are enough columns
                        print(f"Skipping invalid condition row: {row}")
                        continue
                    add_condition(row[1], row[2])

        print(f"Data imported from {filename} successfully!")
    except Exception as e:
        print(f"Error importing from CSV: {e}")
