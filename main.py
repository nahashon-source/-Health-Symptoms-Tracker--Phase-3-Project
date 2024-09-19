import sys
from symptoms import add_symptom, view_symptoms, delete_symptom, update_symptom
from conditions import add_condition, view_conditions, delete_condition, update_condition

def main_menu():
    """Displays the main menu and handles user input for different actions."""
    print("Welcome to the Health Symptoms Tracker")  

    # Main menu loop, runs until the user chooses to exit
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

        # Prompt the user for their choice
        choice = input("\nEnter your choice: ")

        try:
            if choice == '1':
                # Gather input from the user to add a new symptom
                name = input("Symptom Name: ")
                severity = int(input("Severity (1-10): "))
                date = input("Date (YYYY-MM-DD): ")
                notes = input("Notes (optional): ")
                add_symptom(name, severity, date, notes)  # Call the function to add a symptom
                print("Symptom added successfully!")

            elif choice == '2':
                # View all symptoms
                symptoms = view_symptoms()
                # Loop through the retrieved symptoms and print them
                for s in symptoms:
                    print(f"ID: {s[0]}, Name: {s[1]}, Severity: {s[2]}, Date: {s[3]}, Notes: {s[4]}")

            elif choice == '3':
                # Delete a symptom by ID
                symptom_id = int(input("Symptom ID to delete: "))
                delete_symptom(symptom_id)  # Call the function to delete a symptom
                print("Symptom deleted successfully!")

            elif choice == '4':
                # Update an existing symptom
                symptom_id = int(input("Symptom ID to update: "))
                name = input("New Symptom Name: ")
                severity = int(input("New Severity (1-10): "))
                date = input("New Date (YYYY-MM-DD): ")
                notes = input("New Notes (optional): ")
                update_symptom(symptom_id, name, severity, date, notes)  # Call the function to update a symptom
                print("Symptom updated successfully!")

            elif choice == '5':
                # Add a new condition
                name = input("Condition Name: ")
                description = input("Description: ")
                add_condition(name, description)  # Call the function to add a condition
                print("Condition added successfully!")

            elif choice == '6':
                # View all conditions
                conditions = view_conditions()
                # Loop through the retrieved conditions and print them
                for c in conditions:
                    print(f"ID: {c[0]}, Name: {c[1]}, Description: {c[2]}")

            elif choice == '7':
                # Delete a condition by ID
                condition_id = int(input("Condition ID to delete: "))
                delete_condition(condition_id)  # Call the function to delete a condition
                print("Condition deleted successfully!")

            elif choice == '8':
                # Update an existing condition
                condition_id = int(input("Condition ID to update: "))
                name = input("New Condition Name: ")
                description = input("New Description: ")
                update_condition(condition_id, name, description)  # Call the function to update a condition
                print("Condition updated successfully!")

            elif choice == '9':
                # Exit the program
                print("Goodbye!")
                sys.exit()  # Exit the program

            else:
                print("Invalid choice. Please try again.")
        
        # Handle invalid input, such as non-integer inputs for ID or severity
        except ValueError:
            print("Invalid input. Please enter the correct data type.")
        
        # Catch any other exceptions that may occur during execution
        except Exception as e:
            print(f"An error occurred: {e}")

# Ensure the main menu is called when the script is run directly
if __name__ == "__main__":
    main_menu()
