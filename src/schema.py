from py2neo.ogm import GraphObject, Property, RelatedTo
import graphene
from py2neo import Graph

# See https://medium.com/elements/diving-into-graphql-and-neo4j-with-python-244ec39ddd94

graph = Graph( # TODO replace with settings see https://github.com/elementsinteractive/flask-graphql-neo4j/blob/master/app/models.py
    host = "...",
    port = "...",
    user = "...",
    password = "..."
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

class CompoundSchema(graphene.ObjectType):
    inchi = graphene.String()

class Query(graphene.ObjectType):
    compound = graphene.field(lambda: CompoundSchema, inchi=graphene.String())

    def resolve_compound(root,info,inchi):
        # TODO need to add a neo4j node lookup here
        compound = Compound(inchi=inchi).fetch()
        return CompoundSchema(**compound.as_dict())


schema = graphene.Schema(query=Query)