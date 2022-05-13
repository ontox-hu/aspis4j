// assert that edition is community
// assert that version is ge 4.4
CALL apoc.periodic.iterate(
  "CALL apoc.load.csv('file:///CTD_genes_pathways.csv') 
  YIELD list AS line 
  RETURN line",
  "MATCH (g:Gene {GeneID: toInteger(line[1])})
  MATCH (p:Pathway {PathwayID: line[3]})
  CALL apoc.create.relationship(g, 'ASSOCIATED_WITH', {}, p)
  YIELD rel
  RETURN count(rel)",
  {batchSize:1000, parallel:true})