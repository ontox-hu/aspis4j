// assert that edition is community
// assert that version is ge 4.4
CALL apoc.periodic.iterate(
  "CALL apoc.load.csv('file:///CTD_genes_diseases_2000.csv') 
  YIELD list AS line 
  RETURN line",
  "MATCH (g:Gene {GeneID: toInteger(line[1])})
  MATCH (d:Disease {DiseaseID: line[3]})
  CREATE (gd:GeneDisease:Factor {
      DirectEvidence: line[4],
      InferenceChemicalName: line[5],
      InferenceScore: line[6],
      OmimIDs: line[7],
      PubMedIDs: line[8]
      })
  CREATE (g)-[r1:ASSOCIATED_WITH]->(gd)
  CREATE (gd)-[r2:ASSOCIATED_WITH]->(d)
  YIELD rel
  RETURN count(rel)
  ",
  {batchSize:1000, parallel:true})