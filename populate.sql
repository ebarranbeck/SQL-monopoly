/* Ellie Barran Beck, 10328801*/
INSERT INTO Tokens(ID, Name)
VALUES (1,'dog'),
(2,'car'),
(3,'battleship'),
(4,'top hat'),
(5,'thimble'),
(6,'boot')
;

INSERT INTO Bonuses(ID, Name, Description)
VALUES (1, 'Chance 1','Pay each of the other players £50'),
(2,'Chance 2', 'Move forward 3 spaces'),
(3,'Community Chest 1', 'For winning a Beauty Contest, you win £100'),
(4,'Community Chest 2', 'Your library books are overdue. Play a fine of £30'),
(5, 'Free Parking','No action'),
(6,'Go to Jail', 'Go to Jail, do not pass GO, do not collect £200'),
(7,'GO','Collect £200');

INSERT INTO LocationType(ID, Type)
VALUES (1,'corner'),
(2,'chance'),
(3,'community chest'),
(4,'property');


INSERT INTO Location(ID, Name,LocationType)
VALUES (1,'GO',1),
(2,'Kilburn',4),
(3,'Chance 1',2),
(4,'Uni Place',4),
(5,'In Jail',1),
(6,'Victoria',4),
(7,'Community Chest 1',3),
(8,'Piccadilly',4),
(9,' Free Parking',1),
(10,'Oak House',4),
(11, 'Chance 2',2),
(12, 'Owens Park',4),
(13,'Go to Jail',1),
(14,'AMBS',4),
(15,'Community Chest 2',3),
(16,'Co-op',4);

INSERT INTO Players(ID, Name, Token, BankBalance, CurrentLoc, AnyBonus,GameRound)
VALUES (1,'Mary',3,190,9,5,1),
(2,'Bill',1,500,12,NULL,1),
(3,'Jane',2,150,14,NULL,1),
(4,'Norman',5,250,2,NULL,1);

INSERT INTO Properties(ID,Name,Cost,Colour, OwnerID)
VALUES (1,'Oak House',100,'orange',4),
(2,'Owens Park',30,'orange',4),
(3,'AMBS', 400, 'blue', NULL),
(4, 'Co-op', 30,'blue',3),
(5,'Kilburn', 120, 'yellow', NULL),
(6, 'Uni Place', 100, 'yellow', 1),
(7, 'Victoria', 75, 'green' ,2),
(8, 'Piccadilly', 35, 'green', NULL);