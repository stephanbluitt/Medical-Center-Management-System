# Medical-Center-Management-System
A command-line application designed to manage doctors and patients within a medical center.

Features:

Add doctors and patients with unique IDs, names, contact details, and specialties (for doctors).
View lists of registered doctors and patients.
Simple CLI interface with menu-driven navigation.
Structure:

Uses Person class to represent both doctors and patients, with optional specialty field for doctors.
MedicalCenter class handles operations like adding/listing entries and auto-generating unique IDs.
Data is stored in dictionaries during runtime (no persistent storage).
How to Use:
Run the script and follow the menu prompts to add/view entries or exit the program.

Note: This is a basic implementation. Future enhancements could include data persistence (e.g., saving to files) and additional functionalities like search or appointment scheduling.
