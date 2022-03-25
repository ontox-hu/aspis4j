from unicodedata import name
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

class BaseModel(GraphObject):
    """
    Implements some basic functions to guarantee some standard functionality
    across all models. The main purpose here is also to compensate for some
    missing basic features that we expected from GraphObjects, and improve the
    way we interact with them.
    """

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    @property
    def all(self):
        return self.match(graph)

    def save(self):
        graph.push(self)

    def delete(self):
        graph.delete(self)

class Chemical(BaseModel):
    __primarykey__  = 'ChemicalID'
    ChemicalID = Property()     # MeSH Identifier
    ChemicalName = Property()   # CAS Registry Number
    CasRN = Property()

    def fetch(self, _id):
        return self.match(graph, _id).first()

    def fetch_by_ChemicalID(self, ChemicalID):
        return Chemical.match(graph).where(
            f'_.ChemicalID = "{ChemicalID}"'
        ).first()

    def as_dict(self):
        return {
            #'id': self.__primaryvalue__,
            'ChemicalID': self.ChemicalID,
            'ChemicalName': self.ChemicalName,
            'CasRN': self.CasRN
        }

class Protein(BaseModel):
    __primarykey__ = 'uniprot'

class Compound(BaseModel):
    #__primarykey__  = 'id'
    #id = Property()
    pubchem_cid = Property()
    name = Property()
    # compounds have lots of properties, do we have to define them all up front?
    # maybe just passing a reference to pubchem is enough?

    metabolizes  = RelatedTo('Protein',"metabolizes") 
    translocates = RelatedTo('Protein',"translocates")
    is_converted = RelatedTo('Compound','is_converted_to')
    translocated_from = RelatedTo('Compound','translocated_from')

    def fetch(self, _id):
        return self.match(graph, _id).first()

    def as_dict(self):
        return {
            'id': self.__primaryvalue__,
            'pubchem_cid': self.pubchem_cid,
            'name': self.name
        }