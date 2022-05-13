// assert that edition is community
// assert that version is ge 4.4
CALL apoc.periodic.iterate(
  "CALL apoc.load.csv('file:///CTD_genes_diseases.csv') 
  YIELD list AS line 
  RETURN line",
  "MATCH (g:Gene {GeneID: toInteger(line[1])})
  MATCH (d:Disease {DiseaseID: line[3]})
  CALL apoc.create.relationship(g, 'ASSOCIATED_WITH', {
      DirectEvidence: line[4],
      InferenceChemicalName: line[5],
      InferenceScore: line[6],
      OmimIDs: line[7],
      PubMedIDs: line[8]
      }, d)
  YIELD rel
  RETURN count(rel)",
  {batchSize:1000, parallel:true})