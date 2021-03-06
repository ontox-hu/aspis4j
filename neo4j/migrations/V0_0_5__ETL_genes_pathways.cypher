// assert that edition is community
// assert that version is ge 4.4
CALL apoc.periodic.iterate(
  "CALL apoc.load.csv('file:///CTD_genes_pathways_2000.csv') 
  YIELD list AS line 
  RETURN line",
  "MATCH (g:Gene {GeneID: toInteger(line[1])})
  MATCH (p:Pathway {PathwayID: line[3]})
  CREATE (gp:GenePathway:Factor {})
  CREATE (g)-[r1:ASSOCIATED_WITH]->(gp)
  CREATE (gp)-[r2:ASSOCIATED_WITH]->(p)
  RETURN gp
  ",
  {batchSize:1000, parallel:true})