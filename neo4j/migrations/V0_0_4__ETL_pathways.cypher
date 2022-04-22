// assert that edition is community
// assert that version is ge 4.4
LOAD CSV FROM 'file:///CTD_pathways.csv' AS line
CALL {
  WITH line
  CREATE (p:Pathway {
    PathwayID: line[1],
    PathwayName: line[0]
    })
} IN TRANSACTIONS OF 1000 ROWS