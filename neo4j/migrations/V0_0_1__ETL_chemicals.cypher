// assert that edition is community
// assert that version is ge 4.4
LOAD CSV FROM 'file:///CTD_chemicals.csv' AS line
CALL {
  WITH line
  CREATE (c:Chemical {
    ChemicalID: substring(line[1], 5),
    ChemicalName: line[0], 
    CasRN: coalesce(line[2], '')
    })
} IN TRANSACTIONS OF 1000 ROWS