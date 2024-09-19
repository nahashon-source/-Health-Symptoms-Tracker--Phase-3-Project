import sys
from symptoms import add_symptom, view_symptoms, delete_symptom, update_symptom
from conditions import add_condition, view_conditions, delete_condition, update_condition

def main_menu():
    print("Welcome to the Health Symptoms Tracker")
    while True:
        print("\nMain Menu:")
        print("1. Add Symptom")
        print("2. View Symptoms")
        print("3. Delete Symptom")
        print("4. Update Symptom")
        print("5. Add Condition")
        print("6. View Conditions")
        print("7. Delete Condition")
        print("8. Update Condition")
        print("9. Exit")

        choice = input("\nEnter your choice: ")

        try:
            if choice == '1':
                name = input("Symptom Name: ")
                severity = int(input("Severity (1-10): "))
                date = input("Date (YYYY-MM-DD): ")
                notes = input("Notes (optional): ")
                add_symptom(name, severity, date, notes)
                print("Symptom added successfully!")

            elif choice == '2':
                symptoms = view_symptoms()
                for s in symptoms:
                    print(f"ID: {s[0]}, Name: {s[1]}, Severity: {s[2]}, Date: {s[3]}, Notes: {s[4]}")

            elif choice == '3':
                symptom_id = int(input("Symptom ID to delete: "))
                delete_symptom(symptom_id)
                print("Symptom deleted successfully!")

            elif choice == '4':
                symptom_id = int(input("Symptom ID to update: "))
                name = input("New Symptom Name: ")
                severity = int(input("New Severity (1-10): "))
                date = input("New Date (YYYY-MM-DD): ")
                notes = input("New Notes (optional): ")
                update_symptom(symptom_id, name, severity, date, notes)
                print("Symptom updated successfully!")

            elif choice == '5':
                name = input("Condition Name: ")
                description = input("Description: ")
                add_condition(name, description)
                print("Condition added successfully!")

            elif choice == '6':
                conditions = view_conditions()
                for c in conditions:
                    print(f"ID: {c[0]}, Name: {c[1]}, Description: {c[2]}")

            elif choice == '7':
                condition_id = int(input("Condition ID to delete: "))
                delete_condition(condition_id)
                print("Condition deleted successfully!")

            elif choice == '8':
                condition_id = int(input("Condition ID to update: "))
                name = input("New Condition Name: ")
                description = input("New Description: ")
                update_condition(condition_id, name, description)
                print("Condition updated successfully!")

            elif choice == '9':
                print("Goodbye!")
                sys.exit()

            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter the correct data type.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main_menu()  # Ensure the main menu is called
