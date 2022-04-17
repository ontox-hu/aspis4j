// assert that edition is community
// assert that version is ge 4.4
LOAD CSV FROM 'file:///CTD_genes.csv' AS line
CALL {
  WITH line
  CREATE (g:Gene {
    GeneID: toInteger(line[2]), 
    GeneName: line[1], 
    GeneSymbol: line[0],
    AltGeneID: line[3],
    Synonyms: line[4],
    BioGRIDIDs: line[5],
    PharmGKBIDs: line[6],
    UniprotIDs: line[7]
    })
} IN TRANSACTIONS OF 1000 ROWS