
# Amy Saad
# File: gui.py
# Overview: creates a GUI popup window using Tkinter, allowing users to choose from dropdown, 
# menus and display the results in an output box

# Part 2 & 3:
# --------------------------------------------------------------------------------------------------------------------------------------------------

import tkinter as tk                                                                                    # imports tkinter library
from tkinter import ttk                                                                                 # imports ttk module from tkinter for themed widgets
from tkinter import messagebox                                                                          # imports messagebox from tkinter for displaying messages
import sqlite3                                                                                          # imports sqlite3 for SQLite database operations

def fetch_data(dropdowns):                                                                              # function to fetch data based on selected dropdown filter
    try:
        selected_filters = {col: var.get() for col, var in dropdowns.items() if var.get() != "All"}     # creates dictionary of selected filters from dropdown menus
        query = "SELECT * FROM zoo_dataset"                                                             # initializes SQL query
        conditions = []                                                                                 # initializes list to hold conditions for SQL query
        
        for col, value in selected_filters.items():                                                     # iterates over selected filters to build SQL conditions
            if value != "All":
                conditions.append(f"{col} = '{value}'")
        
        if conditions:                                                                                  # adds where clause to SQL query if conditions exist
            query += " WHERE " + " AND ".join(conditions)
        
        connection = sqlite3.connect('zoo_dataset.db')                                                  # connects to SQLite database
        cursor = connection.cursor()                                                                    # creates cursor object to execute SQL queries
        cursor.execute(query)                                                                           # executes SQL query
        rows = cursor.fetchall()                                                                        # fetches all rows from query result
        output_text.delete(1.0, tk.END)                                                                 # clears previous output in output_text 

        for row in rows:
            output_text.insert(tk.END, str(row) + "\n")                                                 # displays new output in output_text 

        connection.close()                                                                              # closes database connection
    
    except sqlite3.Error as e:                                                                          # handles SQLite errors
        messagebox.showerror("Error", f"Error fetching data: {e}")                                      # displays error message using messagebox

root = tk.Tk()                                                                                          # initializes tkinter window
root.title("Zoo Dataset GUI")                                                                           # GUI title

main_frame = ttk.Frame(root, padding="10")                                                              # creates main frame within tkinter window 
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))                                       # places main frame in tkinter window using grid layout 

columns = ['animal_name', 'hair', 'feathers', 'eggs', 'milk', 'airborne', 'aquatic',                    # defines columns for dropdown menus
           'predator', 'toothed', 'backbone', 'breathes', 'venomous', 'fins', 'legs', 
           'tail', 'domestic', 'catsize', 'animal_type']

dropdowns = {}                                                                                          # initializes dictionary to hold dropdown variables
row_num = 0                                                                                             # initializes row and column numbers for grid 
col_num = 0

for col in columns:                                                                                     # loops over columns to create dropdown menus
    label = ttk.Label(main_frame, text=col)                                                             # creates label for dropdown
    label.grid(row=row_num, column=col_num, padx=5, pady=5)                                             # places label in main frame using grid 
    var = tk.StringVar(root)                                                                            # creates string to hold dropdown value
    var.set("All")
    
    connection = sqlite3.connect('zoo_dataset.db')                                                      # connects to SQLite database
    cursor = connection.cursor()                                                                        # creates cursor object to execute SQL queries
    cursor.execute(f"SELECT DISTINCT {col} FROM zoo_dataset")                                           # executes SQL query to get values for dropdown
    values = ["All"] + [item[0] for item in cursor.fetchall()]                                          # fetches values from query result
    connection.close()                                                                                  # closes database connection
    
    dropdown = ttk.Combobox(main_frame, textvariable=var, values=values, width=15)                      # creates dropdown widget
    dropdown.grid(row=row_num, column=col_num+1, padx=5, pady=5)                                        # places dropdown in main frame using grid layout
    dropdowns[col] = var                                                                                # adds to dropdowns dictionary

    row_num += 1                                                                                        # updates row and col numbers for grid placement
    if row_num >= len(columns) // 2:
        row_num = 0
        col_num += 2

fetch_button = ttk.Button(main_frame, text="Execute query", command=lambda: fetch_data(dropdowns))      # creates execute query button
fetch_button.grid(row=len(columns)//2, column=0, columnspan=2, padx=5, pady=5)                          # places execute query button in main frame using grid layout

output_text = tk.Text(main_frame, width=50, height=10)                                                  # creates output text box
output_text.grid(row=len(columns)//2+1, column=0, columnspan=2, padx=5, pady=5)                         # places output text area in main frame using grid layout

root.mainloop()                                                                                         # tkinter loop
