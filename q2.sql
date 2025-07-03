
/* Ellie Barran Beck, 10328801*/
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


