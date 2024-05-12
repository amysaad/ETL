
# Amy Saad
# File: README.TXT 

## Overview
This Python program offers a graphical user interface (GUI) for querying a SQLite database containing a zoo dataset. Users can select filters from dropdown menus, execute SQL queries via the GUI, and view the query results.

## Dependencies
- Python 3.12.0
- Tkinter 
- SQLite3

## Database Information
- Database Name: zoo_dataset.db
- Table Name: zoo_dataset

## How to Run the Program
1. Ensure Python 3.10 or later is installed on your system.
2. Download the program files.
3. Run the `preprocessing.py` file using Python to create the SQLite database for the zoo data.
4. Run the `gui.py` file using Python. The GUI window should open, allowing interaction with the program and enabling SQL query execution to read data from the database.

## How to Use the GUI
1. Select filter from the dropdown menus for various attributes
2. Click the "Execute query" button to execute the SQL query based on the selected filter
3. The results of the query will be displayed in the output text area below the dropdown menus
4. To close the program, either close the GUI window or press Ctrl+C in the terminal where the program is running

## Important Notes
- Ensure that the `preprocessing.py` file runs without issues and does not create duplicates even when executed multiple times
- Closing the GUI window should terminate the program

## Testing
- The program has been tested on a Mac system with Python 3.12.0 and should be compatible with other systems that support Python 3.10 or later

## Additional Information
For any queries or issues, please contact Amy Saad at saad_amy@wheatoncollege.edu