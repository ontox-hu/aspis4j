// assert that edition is community
// assert that version is ge 4.4
USING PERIODIC COMMIT 1000
LOAD CSV WITH HEADERS FROM 'file:///CTD_chemicals.csv' AS row 
MERGE (c:Chemical {ChemicalID: row.ChemicalID, ChemicalName: row.ChemicalName, CasRN: row.CasRN})