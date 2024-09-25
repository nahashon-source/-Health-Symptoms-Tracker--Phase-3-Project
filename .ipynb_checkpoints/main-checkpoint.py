
# import sys
# from datetime import datetime
# from symptoms import add_symptom, view_symptoms, delete_symptom, update_symptom
# from conditions import add_condition, view_conditions, delete_condition, update_condition

# def validate_severity(severity):
#     """Ensures that the severity is between 1 and 10."""
#     try:
#         severity = int(severity)
#         if severity < 1 or severity > 10:
#             raise ValueError("Severity must be between 1 and 10.")
#         return severity
#     except ValueError as e:
#         print(e)
#         return None

# def validate_date(date_str):
#     """Validates the date format (YYYY-MM-DD)."""
#     try:
#         datetime.strptime(date_str, '%Y-%m-%d')
#         return True
#     except ValueError:
#         print("Invalid date format. Please use YYYY-MM-DD.")
#         return False

# def main_menu():
#     """Displays the main menu and handles user input for different actions."""
#     print("Welcome to the Health Symptoms Tracker")

#     while True:
#         print("\nMain Menu:")
#         print("1. Add Symptom")
#         print("2. View Symptoms")
#         print("3. Delete Symptom")
#         print("4. Update Symptom")
#         print("5. Add Condition")
#         print("6. View Conditions")
#         print("7. Delete Condition")
#         print("8. Update Condition")
#         print("9. Exit")

#         choice = input("\nEnter your choice: ")

#         try:
#             if choice == '1':
#                 name = input("Symptom Name: ")
#                 severity = None
#                 while severity is None:
#                     severity = validate_severity(input("Severity (1-10): "))
#                 date = None
#                 while not date:
#                     date_input = input("Date (YYYY-MM-DD): ")
#                     if validate_date(date_input):
#                         date = date_input
#                 notes = input("Notes (optional): ")
#                 add_symptom(name, severity, date, notes)
#                 print("Symptom added successfully!")

#             elif choice == '2':
#                 symptoms = view_symptoms()
#                 for s in symptoms:
#                     print(f"ID: {s[0]}, Name: {s[1]}, Severity: {s[2]}, Date: {s[3]}, Notes: {s[4]}")

#             elif choice == '3':
#                 symptom_id = int(input("Symptom ID to delete: "))
#                 delete_symptom(symptom_id)
#                 print("Symptom deleted successfully!")

#             elif choice == '4':
#                 symptom_id = int(input("Symptom ID to update: "))
#                 name = input("New Symptom Name: ")
#                 severity = None
#                 while severity is None:
#                     severity = validate_severity(input("New Severity (1-10): "))
#                 date = None
#                 while not date:
#                     date_input = input("New Date (YYYY-MM-DD): ")
#                     if validate_date(date_input):
#                         date = date_input
#                 notes = input("New Notes (optional): ")
#                 update_symptom(symptom_id, name, severity, date, notes)
#                 print("Symptom updated successfully!")

#             elif choice == '5':
#                 name = input("Condition Name: ")
#                 description = input("Description: ")
#                 add_condition(name, description)
#                 print("Condition added successfully!")

#             elif choice == '6':
#                 conditions = view_conditions()
#                 for c in conditions:
#                     print(f"ID: {c[0]}, Name: {c[1]}, Description: {c[2]}")

#             elif choice == '7':
#                 condition_id = int(input("Condition ID to delete: "))
#                 delete_condition(condition_id)
#                 print("Condition deleted successfully!")

#             elif choice == '8':
#                 condition_id = int(input("Condition ID to update: "))
#                 name = input("New Condition Name: ")
#                 description = input("New Description: ")
#                 update_condition(condition_id, name, description)
#                 print("Condition updated successfully!")

#             elif choice == '9':
#                 print("Goodbye!")
#                 sys.exit()

#             else:
#                 print("Invalid choice. Please try again.")
        
#         except ValueError:
#             print("Invalid input. Please enter the correct data type.")
        
#         except Exception as e:
#             print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     main_menu()

# main.py

from auth import authenticate_user
from symptoms import (add_symptom, view_symptoms, search_symptoms, 
                       delete_symptom, update_symptom)
from conditions import (add_condition, view_conditions, 
                        delete_condition, update_condition)
from export_import import export_to_csv, import_from_csv

def main_menu():
    """Displays the main menu and handles user input for different actions."""
    print("Welcome to the Health Symptoms Tracker")

    # User Authentication
    username = input("Username: ")
    password = input("Password: ")
    
    if not authenticate_user(username, password):
        print("Authentication failed.")
        return

    # Main menu loop, runs until the user chooses to exit
    while True:
        print("\nMain Menu:")
        print("1. Add Symptom")
        print("2. View Symptoms")
        print("3. Search Symptoms")
        print("4. Delete Symptom")
        print("5. Update Symptom")
        print("6. Add Condition")
        print("7. View Conditions")
        print("8. Delete Condition")
        print("9. Update Condition")
        print("10. Export to CSV")
        print("11. Import from CSV")
        print("12. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Symptom name: ")
            severity = input("Severity (1-10): ")
            date = input("Date (YYYY-MM-DD): ")
            notes = input("Notes: ")
            add_symptom(name, severity, date, notes)

        elif choice == '2':
            symptoms = view_symptoms()
            for symptom in symptoms:
                print(symptom)

        elif choice == '3':
            keyword = input("Enter symptom name to search: ")
            results = search_symptoms(keyword)
            for result in results:
                print(result)

        elif choice == '4':
            symptom_id = input("Enter symptom ID to delete: ")
            delete_symptom(symptom_id)

        elif choice == '5':
            symptom_id = input("Enter symptom ID to update: ")
            name = input("New symptom name: ")
            severity = input("New severity (1-10): ")
            date = input("New date (YYYY-MM-DD): ")
            notes = input("New notes: ")
            update_symptom(symptom_id, name, severity, date, notes)

        elif choice == '6':
            name = input("Condition name: ")
            description = input("Condition description: ")
            add_condition(name, description)

        elif choice == '7':
            conditions = view_conditions()
            for condition in conditions:
                print(condition)

        elif choice == '8':
            condition_id = input("Enter condition ID to delete: ")
            delete_condition(condition_id)

        elif choice == '9':
            condition_id = input("Enter condition ID to update: ")
            name = input("New condition name: ")
            description = input("New description: ")
            update_condition(condition_id, name, description)

        elif choice == '10':
            filename = input("Enter filename for export (e.g., symptoms.csv): ")
            export_to_csv(filename)

        elif choice == '11':
            filename = input("Enter filename for import (e.g., symptoms.csv): ")
            import_from_csv(filename)

        elif choice == '12':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
