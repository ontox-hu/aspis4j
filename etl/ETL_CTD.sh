cd /var/lib/neo4j/import
rm *
sudo wget http://ctdbase.org/reports/CTD_chemicals.csv.gz
sudo wget http://ctdbase.org/reports/CTD_genes.csv.gz
sudo wget http://ctdbase.org/reports/CTD_diseases.csv.gz
sudo wget http://ctdbase.org/reports/CTD_pathways.csv.gz
sudo wget http://ctdbase.org/reports/CTD_chem_gene_ixns.csv.gz
sudo wget http://ctdbase.org/reports/CTD_chemicals_diseases.csv.gz
sudo wget http://ctdbase.org/reports/CTD_genes_pathways.csv.gz
sudo wget http://ctdbase.org/reports/CTD_diseases_pathways.csv.gz
sudo wget http://ctdbase.org/reports/CTD_genes_diseases.csv.gz
sudo gzip -d *.gz
for file in *
do
    tail -n +29 $file > temp.csv 
    mv temp.csv $file
done
for file in *
do
    filename=$(basename -- "$file")
    extension="${filename##*.}"
    filename="${filename%.*}"
    tail -n -2001 $file > temp.csv 
    mv temp.csv "${filename}_2000.csv"
done