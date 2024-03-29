// assert that edition is community
// assert that version is ge 4.4
CALL apoc.periodic.iterate(
  "CALL apoc.load.csv('file:///CTD_chemicals_diseases_2000.csv') 
  YIELD list AS line 
  RETURN line",
  "MATCH (c:Chemical {ChemicalID: line[1]})
  MATCH (d:Disease {DiseaseID: line[4]})
  CREATE (cd:ChemicalDisease:Factor {
      DirectEvidence: line[5],
      InferenceGeneSymbol: line[6],
      InferenceScore: line[7],
      OmimIDs: line[8],
      PubMedIDs: line[9]
      })
  CREATE (c)-[r1:ASSOCIATED_WITH]->(cd)
  CREATE (cd)-[r2:ASSOCIATED_WITH]->(d)
  RETURN cd
  ",
  {batchSize:1000, parallel:true})