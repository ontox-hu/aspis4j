// assert that edition is community
// assert that version is ge 4.4
LOAD CSV FROM 'file:///CTD_genes.csv' AS line 
CALL {
  WITH line
  MATCH (c:Chemical {ChemicalID: line[1]})
  MATCH (g:Gene {GeneID: toInteger(line[4])})
  WITH c, g, line
    UNWIND split(line[9], '|') AS Interaction
    CREATE (c)-[ix:INTERACT {
      Interaction: Interaction,
      GeneForms: line[5],
      Organism: line[6],
      OrganismID: line[7],
      InteractionDetail: line[8],
      PubMedIDs: line[10]
      }]->(g)
} IN TRANSACTIONS OF 1000 ROWS
      
