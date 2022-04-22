// assert that edition is community
// assert that version is ge 4.4
CALL apoc.periodic.iterate(
  "CALL apoc.load.csv('file:///CTD_chemicals_diseases.csv') 
  YIELD list AS line 
  RETURN line",
  "MATCH (c:Chemical {ChemicalID: line[1]})
  MATCH (d:Disease {DiseaseID: line[4]})
  CALL apoc.create.relationship(c, 'ASSOCIATED_WITH', {
      DirectEvidence: line[5],
      InferenceGeneSymbol: line[6],
      InferenceScore: line[7],
      OmimIDs: line[8],
      PubMedIDs: line[9]
      }, d)
  YIELD rel
  RETURN count(rel)",
  {batchSize:1000, parallel:true})