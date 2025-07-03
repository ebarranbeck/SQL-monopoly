/* Ellie Barran Beck, 10328801*/
UPDATE Properties
SET OwnerID=1
WHERE Name='Kilburn';

UPDATE Players
SET BankBalance=BankBalance+80, AnyBonus=NULL, CurrentLoc=2
WHERE Name='Mary';



