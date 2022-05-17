// Check interaction between Chemical and Gene
// given name and symbol
MATCH (c:Chemical)-->(cg:ChemicalGene)-->(g:Gene)
WHERE c.ChemicalName CONTAINS 'Acid' AND g.GeneSymbol = 'ZNF644' 
RETURN cg

// Check interaction between Chemical and Gene
// given IDs
MATCH (c:Chemical {ChemicalID: 'D000077211'})-->(cg:ChemicalGene)-->(g:Gene {GeneID: 127396})
RETURN cg

// Check interaction between Chemical and Gene
// given names
MATCH (c:Chemical {ChemicalID: 'D000077211'})-->(cg:ChemicalGene)-->(g:Gene {GeneID: 127396})
RETURN cg

// Check interaction between Chemical and Gene
// With specific kind of interaction
MATCH (c:Chemical {ChemicalID: 'D000077211'})-->(cg:ChemicalGene {Interaction: 'decreases^expression'})-->(g:Gene {GeneID: 127396})
RETURN cg

