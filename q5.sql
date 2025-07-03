/* Ellie Barran Beck, 10328801*/
UPDATE Players
SET GameRound=2;

UPDATE Players
SET BankBalance=BankBalance+75
WHERE Name='Bill';

UPDATE Players
SET BankBalance=BankBalance-75, CurrentLoc=6, AnyBonus =NULL
WHERE Name='Jane';

