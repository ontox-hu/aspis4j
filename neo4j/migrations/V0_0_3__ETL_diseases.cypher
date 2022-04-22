// assert that edition is community
// assert that version is ge 4.4
LOAD CSV FROM 'file:///CTD_diseases.csv' AS line
CALL {
  WITH line
  CREATE (d:Disease {
    DiseaseID: line[1],
    DiseaseName: line[0], 
    Definition: line[2], 
    AltDiseaseIDs: line[3], 
    Synonyms: line[7], 
    SlimMappings: line[8]
    })
} IN TRANSACTIONS OF 1000 ROWS