from py2neo.ogm import Graph, GraphObject, Property, RelatedTo
from settings import NEO4J_HOST,NEO4J_PASSWORD,NEO4J_PORT,NEO4J_USER

# See https://medium.com/elements/diving-into-graphql-and-neo4j-with-python-244ec39ddd94
# TODO add entities and relationships similar to the ctd schema http://ctdbase.org/
# TODO enforce some uniqueness constraints, choose ids that can be easily linked to by external sources

graph = Graph( 
    host     = NEO4J_HOST,
    port     = NEO4J_PORT,
    user     = NEO4J_USER,
    password = NEO4J_PASSWORD,
    scheme   = "neo4j+s"
)

class Protein(GraphObject):
    __primarykey__ = 'uniprot'


class Compound(GraphObject):
    __primarykey__ = 'inchi'
    inchi          = Property()
    # compounds have lots of properties, do we have to define them all up front?
    # maybe just passing a reference to pubchem is enough?

    metabolizes  = RelatedTo('Protein',"metabolizes") 
    translocates = RelatedTo('Protein',"translocates")
    is_converted = RelatedTo('Compound','is_converted_to')
    translocated_from = RelatedTo('Compound','translocated_from')

    def fetch(self):
        return self.match(graph,self.inchi).first()