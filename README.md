# Monopolee in SQLite
This project included designing and implementing an SQL database based of the scenarios, rules, initial states and gameplay provided. In this file I will provide this along with descriptions of any decision I made. 
## 1. Overview and requirements
### 1.1 Tasks
The tasks of this project included:
1. Create an entity-relationship diagram 
2. Creare a relational database schema diagram
3. Implement SQL files to create and populate the database and simulate the gameplay. 

### 1.2 Scenario
The list below gives the data definition and manipulation requirements for the game. This is deliberately
not written with super-precise wording. When working on real projects, initial drafts of requirements
are rarely complete and unambiguous. If you find any ambiguities, omissions, or imprecision here, make
your own decision about what to do, and mention this decision in your video.
1. There are up to six players.
2. There are six tokens the players can choose from. Each token has a unique name (dog, car, battleship, top hat, thimble, boot).
3. A player must choose one and only one token.
4. Each space on the board is called a location. A location is one of: a corner, a Chance, a Community Chest, or a property.
5. Chance, Community Chest and corners can be grouped together as “bonuses”. Every bonus has a unique id, its name (e.g., “Chance 1”) and a textual description of what it does.
6. Store data about players, properties and bonuses.
7. A property has a unique name, and a purchase cost, which is also the rent payable to the owner if another player lands on it.
8. A property has either one owner or no owner.
9. Each player has a unique id, name, their chosen token, bank balance, their current location, and any bonus that they may have at that location. All this data should have suitable default values and constraints.
10. A bonus can be used by many players. A player has at most one bonus at any time in the gameplay.
11. There must be an audit trail of the gameplay. For each turn taken by a player, the audit trail should store the player’s id, location landed on, current bank balance, and number of the game round.


### 1.3 Rules 
- R1: If a player lands on a property without an owner, they must buy it.
- R2: If player P lands on a property owned by player Q, then P pays Q arent equal to the cost of the property. If Q owns all the properties of a particular colour, P pays double rent.
- R3: If a player is in jail, they must roll a 6 to get out. They immediately roll again.
- R4: If a player lands on or passes GO they receive £200.
- R5: If a player rolls a 6, they move 6 squares; whatever location they land on has no effect. They then get another roll immediately.
- R6: If a player lands on “Go to Jail”, they move to Jail, without passing GO.
- R7: If a player lands on a Chance or Community Chest location, the action described by the bonus happens.

### 1.4 Intial States
**Bonuses**
| Bonus | Description|
|-------|------------|
|Chance 1 | Pay each of the other players £50|
|Chance 2 | Move forward 3 spaces|
|Community Chest 1|For winning a beauty contest you win £100|
|Community Chest 2|Your library books are overdue. Pay a fine of £30|
|Free Parking|No action|
|Go to Jail|Go to Jail, do not pass GO, do not collect £200|
|GO|Collect £200|
|Jail|Must roll a 6 to get out|


**Properties**

**Players**

## 2. Database design
### 2.1 ER diagram
### 2.2 Schema
### 2.3 Decision and assumptions


## 3. Implementation
### 3.1 Files
- create.sql and populate.sql create and populate the database
- q1-q8 simulate the gameplay G1 to G8
- view.sql provides a leaderboard of the gameplay

### 3.2 Database creation (create.sql)
### 3.3 Database population (populate.sql)
### 3.4 Game view (view.sql)
### 3.5 Gameplay (q1.sql-q8.sql)
#### *Game Round 1:*
 **G1 Jane rolls a 3( q1.sql)**
```
UPDATE Players
SET BankBalance= BankBalance+200,
AnyBonus=7,
CurrentLoc=1
WHERE Name='Jane';
```
- Jane lands on GO
    - Update location and bonus to GO
- Collects £200 so adds 200 to her bank balance


#### q2.sql
G2 Norman rolls a 1
```
UPDATE Players
SET BankBalance=BankBalance+50
WHERE Players.Name='Jane';

UPDATE Players
SET BankBalance=BankBalance+50
WHERE Players.Name='Mary';

UPDATE Players
SET BankBalance=BankBalance+50
WHERE Players.Name='Bill';

UPDATE Players
SET BankBalance=BankBalance-150, CurrentLoc=3,  AnyBonus=1
WHERE Players.Name='Norman';
```
- Norman lands on Chance 1
- Update all players bank balance with an extra £50
- Update Normans bank balance losing £150
- Update his location and bonus as Chance 1

#### q3.sql 
G3 Mary rolls a 4
```
UPDATE Players
SET AnyBonus=6, CurrentLoc=13
WHERE Players.Name='Mary';
```
- Mary lands on go to Jail
- Update location and bonus to Jail

#### q4.sql
G4 Bill rolls a 2
```
UPDATE Properties
SET OwnerID=2
WHERE Name='AMBS';

UPDATE Players
SET BankBalance=BankBalance-400, CurrentLoc=14 
WHERE Name='Bill';
```
- Bill lands on AMBS
- Bill buys AMBS as one of the rules of the game is if you land on a property you have to buy it.
- Updates properties table to set the owner of AMBS to Bill
- The property costs £400 so this is taken out of Bills bank balance

#### View of game after round 1
|GameRound|Player|Location|BankBalance|OwnedProperties|
|---|---|---|---|---|
|1|Jane|Go|400|Co-op|
|1|Mary|Go to Jail|240|Uni place|
|1|Bill|AMBS|150|AMBS, Victoria|
|1|Norman|Chance 1|100|Oak House, Owens Park|

*Game Round 2*

