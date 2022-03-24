import graphene
from neo4j_store import Compound

class CompoundSchema(graphene.ObjectType):
    id = graphene.Int()
    pubchem_cid = graphene.String()
    name = graphene.String()

class CreateCompound(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        pubchem_cid = graphene.String(required=True)

    success = graphene.Boolean()
    compound = graphene.Field(lambda: CompoundSchema)

    def mutate(self, info, **kwargs):
        compound = Compound(**kwargs)
        compound.save()

        return CreateCompound(compound=compound, success=True)

class Query(graphene.ObjectType):
    compound = graphene.Field(lambda: CompoundSchema, _id=graphene.String())

    def resolve_compound(root, info, _id):
        # TODO need to add a neo4j node lookup here
        compound = Compound(_id=_id).fetch(int(_id))
        return CompoundSchema(**compound.as_dict())

    #def resolve_compounds(self, info):
    #    return [CompoundSchema(**compound.as_dict()) for compound in Compound().all]

class Mutations(graphene.ObjectType):
    create_compound = CreateCompound.Field()

schema = graphene.Schema(query=Query, mutation=Mutations).graphql_schema