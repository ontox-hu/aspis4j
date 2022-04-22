// assert that edition is community
// assert that version is ge 4.4
CALL apoc.periodic.iterate("
  CALL apoc.load.csv('file:///CTD_chem_gene_ixns.csv') 
  YIELD list AS line 
  RETURN line
  ",
  "MATCH (c:Chemical {ChemicalID: line[1]})
  MATCH (g:Gene {GeneID: toInteger(line[4])})
  UNWIND split(line[9], '|') AS Interaction
  CALL apoc.create.relationship(c, Interaction, {
      GeneForms: coalesce(line[5], ''),
      Organism: line[6],
      OrganismID: line[7],
      InteractionDetail: line[8],
      PubMedIDs: line[10]
      }, g)
  YIELD rel
  RETURN count(rel)
  ",
  {batchSize:1000, parallel:true})
      
