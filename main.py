# RACHITHA R PAI
# CANARA ENGINEERING COLLEGE, MANGALORE

import sqlite3
import sys
import os
os.system("")
from time import sleep

# Database Connection
def DataBaseConnect():
    return sqlite3.connect("dtbase.db")
db = DataBaseConnect()
cursor = DataBaseConnect().cursor()

# Insert Data into Database
def insert_Data(db):
    movie_name = input("Enter Movie Name: ")
    actor_name = input("Enter Actor's Name: ")
    actress_name = input("Enter actress' Name: ")
    director_name = input("Enter director's Name: ")
    year = input("Enter the year of release: ")
    cmd=("""INSERT INTO database (movie,actor,actress,director,year) VALUES (?,?,?,?,?);""")
    parms=(movie_name,actor_name,actress_name,director_name,year)
    cursor.execute(cmd,parms)
    db.commit()
    print("\nData is Saved : ) ")


# Remove data from Database
def remove_Data(db):
    cursor.execute("""DELETE FROM database;""").fetchall()
    db.commit()
    print("Data is Deleted !")


# Find Movies using Actor's name
def using_Actor():
    act = str(input("Enter Actor's Name : "))
    c = cursor.execute("""SELECT movie FROM database WHERE actor=(?);""",(act,)).fetchall()
    db.commit()
    for i in c:
        print(i,end='')
    if c==[]:
        print("No Such Actor is Found : (")


# Finding Movies using Actress's name
def using_Actress():
    act = str(input("Enter Actress's Name : "))
    c = cursor.execute("""SELECT movie FROM database WHERE actress=(?);""",(act,)).fetchall()
    db.commit()
    for i in c:
        print(i,end='')
    if c==[]:
         print("No Such Actress is Found : (")



# Finding Movies using Director's name
def using_Director():
    director = str(input("Enter the Director's name : "))
    c = cursor.execute("""SELECT movie FROM database WHERE director=(?);""",(director,)).fetchall()
    db.commit()
    for i in c:
        print(i,end='')
    if c==[]:
         print("No Such Dicrector is Found : (")

# Finding Movies using Year of Release
def using_Year():
    year =str(input("Enter the release year : "))
    c=cursor.execute("""SELECT movie FROM database WHERE year=(?);""",(year,)).fetchall()
    db.commit()
    for i in c:
        print(i,end='')
    if c==[]:
         print("No Such Movie is Found : (")



# Database
def displayDataBase():
    Movie =  []
    Actor = []
    Actress  = []
    Director = []
    Year = []
    data = cursor.execute("""SELECT * FROM database; """).fetchall()
    print("Movie" + " | " + "Actor" + " | " + "Actress" + " | " + "Director" + " | " + "Year")
    # printing the data
    for row in data:
        Movie.append(row[0])
        Actor.append(row[1])
        Actress.append(row[2])
        Director.append(row[3])
        Year.append(row[4])
    print("Movie = ", Movie)
    print("Actor = ", Actor)
    print("Actress  = ",Actress)
    print("Director  = ", Director)
    print("Year  = ", Year)


# Creating the Table
def create_Table(db):
    t = cursor.execute("""SELECT * FROM sqlite_master WHERE type='table' and name="database" ; """).fetchall()
    if t==[]:
        cursor.execute("""CREATE TABLE IF NOT EXISTS database(movie VARCHAR(50),actor VARCHAR(20), actress VARCHAR(20), director VARCHAR(20),year INT);""")
        print('Table Created !')
        db.commit()
    else:
        print('Table Already Exist : (')

# checking the Database connection
def check_Connection():
    if DataBaseConnect() is not None:
        print("Connected : )")
        create_Table(DataBaseConnect())
    else:
        print("Sed, No DB not connected : (")
# clear
def clrscr():
    os.system('cls' if os.name=='nt' else 'clear')


# Main
def main():
    while(1):
        clrscr()
        print(" \n\n ..................................................................")
        print("                    Rachitha's Movie Database                      ")
        print(" ..................................................................")
        print(" 1. Checking Database Connection                     ")
        print(" 2. Insert the data                                  ")
        print(" 3. Delete the data                                  ")
        print(" 4. Show the data                                    ")
        print(" 5. Search Movies using Actor's name                 ")
        print(" 6. Search Movies using Actress' name                ")
        print(" 7. Search Movies using Director's name              ")
        print(" 8. Search Movies using the year of release          ")
        print(" 9. Exit                                             ")
        print(" ..................................................................")
        choice=input("\nEnter your Choice ")
        print('..................................................................')
        if choice=='1':
            clrscr()
            check_Connection()
            sleep(3)
        elif choice=='2':
            clrscr()
            insert_Data(DataBaseConnect())
            sleep(3)
        elif choice=='3':
            clrscr()
            remove_Data(DataBaseConnect())
            sleep(3)
        elif choice=='4':
            clrscr()
            displayDataBase()
            sleep(15)
        elif choice=='5':
            clrscr()
            using_Actor()
            sleep(3)
        elif choice=='6':
            clrscr()
            using_Actress()
            sleep(3)
        elif choice=='7':
            clrscr()
            using_Director()
            sleep(3)
        elif choice=='8':
            clrscr()
            using_Year()
            sleep(3)
        elif choice=='9':
            clrscr()
            print("THE END")
            sleep(3)
            exit()
            break
        else:
            clrscr()
            print("Invalid Choice !")
            sleep(3)
main()

