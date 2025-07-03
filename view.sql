/* Ellie Barran Beck, 10328801*/
CREATE VIEW gameView AS
SELECT Players.GameRound,Players.Name AS Player, Location.Name AS Location,Players.BankBalance,GROUP_CONCAT(Properties.Name) AS OwnedProperties
FROM Players
INNER JOIN Location ON Players.CurrentLoc=Location.ID
LEFT JOIN Properties ON Players.ID=Properties.OwnerID
GROUP BY Players.Name
ORDER BY BankBalance DESC;



