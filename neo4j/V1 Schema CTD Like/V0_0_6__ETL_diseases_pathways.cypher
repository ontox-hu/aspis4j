// assert that edition is community
// assert that version is ge 4.4
CALL apoc.periodic.iterate(
  "CALL apoc.load.csv('file:///CTD_diseases_pathways.csv') 
  YIELD list AS line 
  RETURN line",
  "MATCH (d:Disease {DiseaseID: line[1]})
  MATCH (p:Pathway {PathwayID: line[3]})
  CALL apoc.create.relationship(d, 'ASSOCIATED_WITH', {
      InferenceGeneSymbol: line[4]
      }, p)
  YIELD rel
  RETURN count(rel)",
  {batchSize:1000, parallel:true})