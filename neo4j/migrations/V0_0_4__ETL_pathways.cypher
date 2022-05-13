// assert that edition is community
// assert that version is ge 4.4
LOAD CSV FROM 'file:///CTD_pathways_2000.csv' AS line
CALL {
  WITH line
  CREATE (p:Pathway:Variable {
    PathwayID: line[1],
    PathwayName: line[0]
    })
} IN TRANSACTIONS OF 1000 ROWS