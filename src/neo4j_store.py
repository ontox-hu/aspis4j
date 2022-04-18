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
    """
    Chemical Class using CTD Model with properties ChemicalID, 
    ChemicalName and CasRN.
    """

    __primarykey__  = 'ChemicalID'
    ChemicalID = Property()     # MeSH Identifier
    ChemicalName = Property()   # CAS Registry Number
    CasRN = Property()

    def fetch(self, ChemicalID):
        return self.match(graph, ChemicalID).first()

    def as_dict(self):
        return {
            #'id': self.__primaryvalue__,
            'ChemicalID': self.ChemicalID,
            'ChemicalName': self.ChemicalName,
            'CasRN': self.CasRN
        }

class Gene(BaseModel):
    """
    Gene Class using CTD Model with properties GeneID, 
    GeneSymbol, GeneName and Alternative IDs
    """

    __primarykey__  = 'GeneID'
    GeneID = Property()      # NCBI Gene identifier
    GeneSymbol = Property()  # CAS Registry Number
    GeneName = Property()   
    AltGeneIDs = Property()  # alternative NCBI Gene identifiers; '|'-delimited list  
    # TODO: Delimited lists currently in a single string should be replaced by a list structure
    Synonyms = Property()    # '|'-delimited list  
    BioGRIDIDs = Property()  # '|'-delimited list  
    PharmGKBIDs = Property() # '|'-delimited list  
    UniprotIDs = Property()  # '|'-delimited list  

    def fetch(self, GeneID):
        return self.match(graph, GeneID).first()

    def as_dict(self):
        return {
            'GeneID': self.GeneID,
            'GeneSymbol': self.GeneSymbol,
            'GeneName': self.GeneName,
            'Synonyms': self.Synonyms,
            'BioGRIDIDs': self.BioGRIDIDs,
            'PharmGKBIDs': self.PharmGKBIDs,
            'UniprotIDs': self.UniprotIDs
        }

class Disease(BaseModel):
    """
    Disease Class using CTD Model with properties DiseaseID, 
    DiseaseName, Definition and AltDiseaseIDs
    """

    __primarykey__  = 'DiseaseID'
    DiseaseID = Property()    # MeSH or OMIM identifier
    DiseaseName = Property()  
    Definition = Property()   
    # TODO: Delimited lists currently in a single string should be replaced by a list structure
    AltDiseaseIDs = Property()  # alternative identifiers; '|'-delimited list  
    Synonyms = Property()    # '|'-delimited list  
    SlimMappings = Property()  # '|'-delimited list  

    def fetch(self, DiseaseID):
        return self.match(graph, DiseaseID).first()

    def as_dict(self):
        return {
            'DiseaseID': self.DiseaseID,
            'DiseaseName': self.DiseaseName,
            'Definition': self.Definition,
            'AltDiseaseIDs': self.AltDiseaseIDs,
            'Synonyms': self.Synonyms,
            'SlimMappings': self.SlimMappings
        }

class Pathway(BaseModel):
    """
    Pathway Class using CTD Model with properties PathwayID and PathwayName
    """

    __primarykey__  = 'PathwayID'
    PathwayID = Property()    # MeSH or OMIM identifier
    PathwayName = Property()  

    def fetch(self, PathwayID):
        return self.match(graph, PathwayID).first()

    def as_dict(self):
        return {
            'PathwayID': self.PathwayID,
            'PathwayName': self.PathwayName
        }


class Collection(BaseModel):
    """
    Disease Class using CTD Model with properties GeneID, 
    GeneSymbol, GeneName and Alternative IDs
    """

    __primarykey__  = 'CollectionID'
    CollectionID = Property()

    def fetch(self, Collection):
        return self.match(graph, Collection).first()
    
    def as_dict(self):
            return {
            'CollectionID': self.CollectionID
        }
    
