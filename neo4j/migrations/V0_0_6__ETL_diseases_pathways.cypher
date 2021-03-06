// assert that edition is community
// assert that version is ge 4.4
CALL apoc.periodic.iterate(
  "CALL apoc.load.csv('file:///CTD_diseases_pathways_2000.csv') 
  YIELD list AS line 
  RETURN line",
  "MATCH (d:Disease {DiseaseID: line[1]})
  MATCH (p:Pathway {PathwayID: line[3]})
  CREATE (dp:DiseasePathway:Factor {InferenceGeneSymbol: line[4]})
  CREATE (d)-[r1:ASSOCIATED_WITH]->(dp)
  CREATE (dp)-[r2:ASSOCIATED_WITH]->(p)
  RETURN dp
  ",
  {batchSize:1000, parallel:true})