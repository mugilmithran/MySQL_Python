import mysql.connector
from datetime import datetime

# Connecting the created Database
db = mysql.connector.connect(
    host="localhost",
    user="mugil",
    password="Mithran*#123",
    database="testdatabase"
)

mycursor = db.cursor()

# Creating Database
mycursor.execute("CREATE DATABASE testdatabase")

# Creating Table
mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")

# Checking the elements of the Person Table
mycursor.execute("DESCRIBE Person")

for x in mycursor:
    print(x)

# Inserting values to the created table Person
mycursor.execute("INSERT INTO Person (name, age) VALUES (%s, %s)", ("Mugil", 23))
db.commit()

mycursor.execute("INSERT INTO Person (name, age) VALUES (%s, %s)", ("Joe", 25))
db.commit()

# Printing all the values from the Person table
mycursor.execute("SELECT * FROM Person")

for x in mycursor:
    print(x)

# Creating a table Test
mycursor.execute("CREATE TABLE Test (name VARCHAR(50) NOT NULL, created datetime NOT NULL, gender ENUM('M', 'F', 'o') NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")

# Inserting values into the table Test and saving it.
mycursor.execute("INSERT INTO TEST (name, created, gender) VALUES (%s, %s, %s)", ("Mugil", datetime.now(), "M"))
mycursor.execute("INSERT INTO TEST (name, created, gender) VALUES (%s, %s, %s)", ("Joey", datetime.now(), "F"))
db.commit()

# Querying the table for all values where the gender is 'M', by descending order
mycursor.execute("SELECT * FROM Test WHERE gender = 'M' ORDER BY id DESC")

# Querying the table for id and name values where the gender is 'M', by descending order
mycursor.execute("SELECT id, name FROM Test WHERE gender = 'M' ORDER BY id DESC")
for x in mycursor:
    print(x)

#Adding column 'food' to the existing table Test
mycursor.execute("ALTER TABLE Test ADD COLUMN food VARCHAR(50) NOT NULL")

mycursor.execute("DESCRIBE Test")
for x in mycursor:
    print(x)

# Removing the column 'food'
mycursor.execute("ALTER TABLE Test DROP food")

# Renaming column 'name' into 'first_name'
mycursor.execute("ALTER TABLE Test CHANGE name first_name VARCHAR(50)")

# Checking the elements of Test table
mycursor.execute("DESCRIBE Test")
for x in mycursor:
    print(x)


users = [("tim", "techwithtim"),
         ("joe", "joey123"),
         ("sarah", "sarah1234")]

user_scores = [(45, 100),
               (30, 200),
               (46, 124)]

mycursor = db.cursor()

# Saving queries in variables
Q1 = "CREATE TABLE Users (id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), password VARCHAR(50))"
Q2 = "CREATE TABLE Scores (userId int PRIMARY KEY, FOREIGN KEY(userId) REFERENCES Users(id), game1 int DEFAULT 0, game2 int DEFAULT 0)"

# Creating tables named as Users and Scores
mycursor.execute(Q1)
mycursor.execute(Q2)

# Checking the tables that are created
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

# Inserting multiple values into users table at once
mycursor.executemany("INSERT INTO Users (name, password) VALUES (%s, %s)", (users))

# Saving queries as variables
Q3 = "INSERT INTO Users (name, password) VALUES (%s, %s)"
Q4 = "INSERT INTO Scores (userId, game1, game2) VALUES (%s, %s, %s)"

# Inserting values in both the tables
for x, user in enumerate(users):
    mycursor.execute(Q3, user)
    last_id = mycursor.lastrowid
    mycursor.execute(Q4, (last_id,) + user_scores[x])

# Saving
db.commit()

# Fetching all the values from Users table
mycursor.execute("SELECT * FROM Users")
for x in mycursor:
    print(x)

# Fetching all the values from Scores table
mycursor.execute("SELECT * FROM Scores")
for x in mycursor:
    print(x)
