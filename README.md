# -Health-Symptoms-Tracker--Phase-3-Project

# Overview
This is a simple Health Symptoms Tracker application built using Python and PostgreSQL. The tracker helps users manage symptoms and associated conditions by adding, viewing, updating, and deleting records from a database. It uses a command-line interface (CLI) and basic SQL operations.


# Features
1. Symptom management: Add, view, update, and delete symptoms.
2. Condition management: Add, view, update, and delete conditions.
3. Track severity: Record symptom severity and relevant notes.
4. Many-to-Many Relationships: Symptoms can be associated with multiple conditions.


# Requirements
. Python 3.x
. PostgreSQL
. psycopg2 (for connecting to PostgreSQL)


# Install dependencies:
<!-- bash -->
pip install psycopg2

# Database Setup
1. Create the database in PostgreSQL:
<!-- sql -->
CREATE DATABASE tracker;

2. Create tables by running:
<!-- bash -->
python database.py


# How to Run
1. Start the main application:
<!-- bash -->
python main.py

2. Follow the menu prompts to:
. Add, view, update, or delete Symptoms.
. Add, view, update, or delete Conditions.

# File Structure
1. main.py: Entry point of the application, displaying the main menu for user interaction.
2. symptoms.py: Contains functions to manage symptoms (add, view, update, delete).
3. conditions.py: Contains functions to manage conditions (add, view, update, delete).
4. database.py: Manages the connection to the PostgreSQL database and table creation.

# Example
<!-- bash -->
Welcome to the Health Symptoms Tracker

Main Menu:
1. Add Symptom
2. View Symptoms
3. Delete Symptom
4. Update Symptom
5. Add Condition
6. View Conditions
7. Delete Condition
8. Update Condition
9. Exit

# Summary
The Health Symptoms Tracker is a Python-based CLI tool designed to help users track their health symptoms and related conditions. It allows users to log symptoms with severity levels, keep notes, and associate symptoms with conditions using a PostgreSQL database. This project is a great introduction to database management and CRUD (Create, Read, Update, Delete) operations through Python.

