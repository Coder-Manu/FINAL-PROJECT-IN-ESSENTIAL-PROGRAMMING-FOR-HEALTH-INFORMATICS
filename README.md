# Hospital Data Management System

This is a Python-based graphical user interface (GUI) application for managing patient records and handling various operations in a hospital setting. The application is built using the Tkinter library for creating the user interface.

## Features

- User authentication with different roles (management, admin, nurse, clinician)
- Management users can generate key statistics
- Admin users can count visits on a specific date
- Nurse and clinician users can:
 - Retrieve patient visits by patient ID
 - Add new patient records
 - Remove patient records
 - Count visits on a specific date
- Usage logging for tracking user actions

## Files

- `ui.py`: The main file containing the `Application` class and the Tkinter GUI code.
- `authentication.py`: Handles user authentication and credential management.
- `patient_record.py`: Deals with patient record operations (retrieve, add, remove, count visits, generate statistics).
- `PA3_credentials.txt`: A text file containing user credentials (username and password).
- `PA3_patients.csv`: A CSV file containing patient records.
- `usage_log.csv`: A CSV file that logs user actions with timestamps.

## Prerequisites

- Python 3.x
- Required Python libraries: `tkinter`, `datetime`, `os`, `csv`

## Usage

1. Make sure you have the necessary files (`ui.py`, `authentication.py`, `patient_record.py`, `PA3_credentials.txt`, `PA3_patients.csv`) in the same directory.
2. Run the `ui.py` file using Python:
3. The application window will open, prompting you to enter your username and password.
4. After successful authentication, the main menu will be displayed based on your user role.
5. Navigate through the available options using the buttons and follow the prompts to perform various actions.
6. The `usage_log.csv` file will be updated with user actions and timestamps.

## Note

- The `PA3_credentials.txt` file should contain username and password pairs, separated by a comma, with one pair per line (e.g., `username1,password1`).
- The `PA3_patients.csv` file should have the following column headers: `Patient_ID`, `Visit_ID`, `Visit_time`, `Visit_department`, `Race`, `Gender`, `Ethnicity`, `Age`, `Zip_code`, `Insurance`, `Chief_complaint`, `Note_ID`, `Note_type`.

Feel free to modify the code and data files as per your requirements.

Made by Lourdhu Manoj Kataru.
