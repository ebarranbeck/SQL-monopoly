####
# DATA70141 Monopolee Checker
# v1: October 2023
# Tom Carroll
#
####### What is it? #####
# This will help you decide if your SQL filesfor submission are named correctly, 
# and that the changes made by your queries are visible for marking.
# It will NOT tell you if you have the correct output!
#
###### How do I run it? #####
# Place this file in the same directory as your SQL files.
# In your terminal, issue the following command: "python3 monopoleeChecker.py"
# You may need to also run "pip3 install sqlite3"
#
# This script is a reduced functionality version of my marking script, which I will use
# to run your SQL files and determine if the databse functions as required. 
# The marking script I will use is based on this checker script, and has many extra features, such as unit testing 
# and examination of files and the state of the database.
# Basically.... if this checker script can read your files, execute your SQL, and show the state of the database, 
# then the automated marking will work.
# However, I will also use manual examination of your files, aswell as manual examination of the datanbase, 
# if this is needed.

import sqlite3

connection = ''
c = ''


def showView():
    c.execute("SELECT * FROM gameView")
    rows = c.fetchall()

    for r in rows:
        print(r)
    print("\n")



#Read in the Required Files
#CREATE
createSQLFile = open('create.sql', "r")
createSQL = createSQLFile.read()
createSQLFile.close()

print("This is your create.sql file contents: \n")
print(createSQL)
print("\n\n")


#INSERT
insertSQLFile = open('populate.sql', "r")
insertSQL = insertSQLFile.read()
insertSQLFile.close()

print("This is your populate.sql file contents: \n")
print(insertSQL)
print("\n\n")

#VIEW
viewSQLFile = open('view.sql', "r")
viewSQL = viewSQLFile.read()
viewSQLFile.close()

print("This is your veiw.sql file contents: \n")
print(viewSQL)
print("\n\n")

#Q1
q1SQLFile = open('q1.sql', "r")
q1SQL = q1SQLFile.read()
q1SQLFile.close()

print("This is your q1.sql file contents: \n")
print(q1SQL)
print("\n\n")

#Q2
q2SQLFile = open('q2.sql', "r")
q2SQL = q2SQLFile.read()
q2SQLFile.close()

print("This is your q2.sql file contents: \n")
print(q2SQL)
print("\n\n")

#Q3
q3SQLFile = open('q3.sql', "r")
q3SQL = q3SQLFile.read()
q3SQLFile.close()

print("This is your q3.sql file contents: \n")
print(q3SQL)
print("\n\n")

#Q4
q4SQLFile = open('q4.sql', "r")
q4SQL = q4SQLFile.read()
q4SQLFile.close()

print("This is your q4.sql file contents: \n")
print(q4SQL)
print("\n\n")


#Q5
q5SQLFile = open('q5.sql', "r")
q5SQL = q5SQLFile.read()
q5SQLFile.close()

print("This is your q5.sql file contents: \n")
print(q5SQL)
print("\n\n")


#Q6
q6SQLFile = open('q6.sql', "r")
q6SQL = q6SQLFile.read()
q6SQLFile.close()

print("This is your q6.sql file contents: \n")
print(q6SQL)
print("\n\n")


#Q7
q7SQLFile = open('q7.sql', "r")
q7SQL = q7SQLFile.read()
q7SQLFile.close()

print("This is your q7.sql file contents: \n")
print(q7SQL)
print("\n\n")


#Q8
q8SQLFile = open('q8.sql', "r")
q8SQL = q8SQLFile.read()
q8SQLFile.close()

print("This is your q8.sql file contents: \n")
print(q8SQL)
print("\n\n")

#Setup the Database
connection = sqlite3.connect(":memory:")
c = connection.cursor()


#Create DB, populate with data, and create the view
c.executescript(createSQL)
c.executescript(insertSQL)
c.executescript(viewSQL)

#Show Leaderboard gameView as of the initial state
showView()

#####
# ROUND 1
####
print("####### ROUND 1 ######")

print("Query 1 (Jane Rolls a 3): \n")
c.executescript(q1SQL)
showView()


print("Query 2 (Norman Rolls a 1): \n")
c.executescript(q2SQL)
showView()

print("Query 3 (Mary Rolls a 4): \n")
c.executescript(q3SQL)
showView()

print("Query 4 (Bill Rolls a 2): \n")
c.executescript(q4SQL)
showView()

print("####### Round 2 #######")

print("Query 5 (Jane Rolls a 5): \n")
c.executescript(q5SQL)
showView()

print("Query 6 (Norman Rolls a 4): \n")
c.executescript(q6SQL)
showView()

print("Query 7 (Mary rolls a 6, then 5): \n")
c.executescript(q7SQL)
showView()

print("Query 8 (Bill rolls a 6, then 3): \n")
c.executescript(q8SQL)
showView()

print("=============================\n END")


#Close connection, in-mem DB is deleted
connection.close()
