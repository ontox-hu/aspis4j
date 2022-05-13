cd ~/aspis4j/
source vars.sh
cd ~/aspis4j/neo4j/migrations/
cypher-shell -a neo4j+s://aspis4j.com:7687 -d aspis4j -f V0_0_1__ETL_chemicals.cypher
cypher-shell -a neo4j+s://aspis4j.com:7687 -d aspis4j -f V0_0_2__ETL_genes.cypher
cypher-shell -a neo4j+s://aspis4j.com:7687 -d aspis4j -f V0_0_3__ETL_diseases.cypher
cypher-shell -a neo4j+s://aspis4j.com:7687 -d aspis4j -f V0_0_4__ETL_pathways.cypher
cypher-shell -a neo4j+s://aspis4j.com:7687 -d aspis4j -f V0_0_5__ETL_genes_pathways.cypher
cypher-shell -a neo4j+s://aspis4j.com:7687 -d aspis4j -f V0_0_6__ETL_diseases_pathways.cypher
cypher-shell -a neo4j+s://aspis4j.com:7687 -d aspis4j -f V0_0_7__ETL_chem_gene_ixns.cypher
cypher-shell -a neo4j+s://aspis4j.com:7687 -d aspis4j -f V0_0_8__ETL_chemicals_diseases.cypher
cypher-shell -a neo4j+s://aspis4j.com:7687 -d aspis4j -f V0_0_9__ETL_genes_diseases.cypher
