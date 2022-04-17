// assert that edition is community
// assert that version is ge 4.4
USING PERIODIC COMMIT 1000
LOAD CSV WITH HEADERS FROM 'file:///CTD_chem_gene_ixns.csv' AS row
MATCH (c:Chemical {ChemicalID: row.ChemicalID})
MATCH (g:Gene {GeneID: row.GeneID})
WITH c, g, row
UNWIND split(row.Interactions, '|') AS Interaction
MERGE (c)-[ix:Interaction]->(g)
  ON CREATE 
    SET 
      ix.GeneForms = row.GeneForms,
      ix.Organism = row.Organism,
      ix.OrganismID = row.OrganismID,
      ix.InteractionDetail = row.InteractionDetail,
      ix.PubMedIDs = row.PubMedIDs,

      
