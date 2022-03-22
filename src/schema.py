import graphene
from neo4j_store import Compound

class CompoundSchema(graphene.ObjectType):
    inchi = graphene.String()

class Query(graphene.ObjectType):
    compound = graphene.Field(lambda: CompoundSchema, inchi=graphene.String())

    def resolve_compound(root,info,inchi):
        # TODO need to add a neo4j node lookup here
        compound = Compound(inchi=inchi).fetch()
        return CompoundSchema(**compound.as_dict())


schema = graphene.Schema(query=Query).graphql_schema