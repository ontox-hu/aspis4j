// assert that edition is community
// assert that version is ge 4.4
CALL apoc.periodic.iterate("
  CALL apoc.load.csv('file:///CTD_chem_gene_ixns_2000.csv') 
  YIELD list AS line 
  RETURN line
  ",
  "MATCH (c:Chemical {ChemicalID: line[1]})
  MATCH (g:Gene {GeneID: toInteger(line[4])})
  UNWIND split(line[9], '|') AS Interaction
  CREATE (cg:ChemicalGene:Factor {
      Interaction: Interaction,
      GeneForms: coalesce(line[5], ''),
      Organism: line[6],
      OrganismID: line[7],
      InteractionDetail: line[8],
      PubMedIDs: line[10]
      })
  CREATE (c)-[r1:ASSOCIATED_WITH]->(cg)
  CREATE (cg)-[r2:ASSOCIATED_WITH]->(g)
  RETURN cg
  ",
  {batchSize:1000, concurrency:28, parallel:true})
      
