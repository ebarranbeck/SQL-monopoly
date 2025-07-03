# Monopolee in SQLite
The task was to model the gameplay of a simplified version of Monopoly using a relational database and SQL queries. For this I utilised SQLite.

## Game description
### Rules 
R1 If a player lands on a property without an owner, they must buy it.
R2 If player P lands on a property owned by player Q, then P pays Q a
rent equal to the cost of the property. If Q owns all the properties of a
particular colour, P pays double rent.
R3 If a player is in jail, they must roll a 6 to get out. They
immediately roll again.
R4 If a player lands on or passes GO they receive £200.
R5 If a player rolls a 6, they move 6 squares; whatever location they
land on has no effect. They then get another roll immediately.
R6 If a player lands on “Go to Jail”, they move to Jail, without passing
GO.
R7 If a player lands on a Chance or Community Chest location, the action
described by the bonus happens. 
### Gameplay
Gameplay Round 1:
G1 Jane rolls a 3
G2 Norman rolls a 1
G3 Mary rolls a 4
G4 Bill rolls a 2
Gameplay Round 2:
G5 Jane rolls a 5
G6 Norman rolls a 4
G7 Mary rolls a 6, and then a 5
G8 Bill rolls a 6, and then a 3

## ER diagram
### Tables
- Players
- Bonuses
- Tokens
- Location
- Location Type
- Properties
- Audit trail

## Schema


