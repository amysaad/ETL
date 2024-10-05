
# Amy Saad
# File: preprocessing.py
# Overview: connects to an SQLite database and imports a CSV file containing zoo animal data, 
# creating a table in the database and populating it with the data

# Part 1:
# -------------------------------------------------------------------------------------------------------------------------------------------

import sqlite3                                                             # import the python-specific sqlite library
import csv                                                                 # import csv library for file I/O

connection = sqlite3.connect("zoo_dataset.db")                             # connects to SQLite database 

cursor = connection.cursor()                                               # creates cursor object to execute SQL commands

                                                                           # creates table in database if it doesn't already exist
cursor.execute("""  
CREATE TABLE IF NOT EXISTS zoo_dataset (animal_name TEXT, hair INTEGER,
feathers INTEGER, eggs INTEGER, milk INTEGER, airborne INTEGER,
aquatic INTEGER, predator INTEGER, toothed INTEGER, backbone INTEGER,
breathes INTEGER, venomous INTEGER, fins INTEGER, legs INTEGER,
tail INTEGER, domestic INTEGER, catsize INTEGER, animal_type INTEGER)""")  

connection.commit()                                                        # commits changes to the database

with open('zoo.csv', 'r') as file:                                         # opens the CSV file containing the dataset
    csv_reader = csv.reader(file)                                          # creates a CSV reader object
    next(csv_reader)                                                       # skips header row

    for row in csv_reader:                                                 # iterates over each row in CSV file
        animal_name, hair, feathers, eggs, \
        milk, airborne, aquatic, predator, \
        toothed, backbone, breathes, venomous, \
        fins, legs, tail, domestic, catsize, \
        animal_type = row
        
                                                                           # inserts data into the database table
        cursor.execute("""                       
        INSERT INTO zoo_dataset (animal_name, 
        hair, feathers, eggs, milk, airborne, 
        aquatic, predator, toothed, backbone, 
        breathes, venomous, fins, legs, tail, 
        domestic, catsize, animal_type)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
        ?, ?, ?, ?, ?, ?, ?, ?)
        """, (animal_name, int(hair), int(feathers), 
              int(eggs), int(milk), int(airborne), 
              int(aquatic), int(predator), int(toothed), 
              int(backbone), int(breathes), int(venomous), 
              int(fins), int(legs), int(tail), int(domestic), 
              int(catsize), int(animal_type)))


connection.commit()                                                       # commits changes to the database

 
