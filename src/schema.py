import graphene
from neo4j_store import Chemical
from neo4j_store import Compound

class ChemicalSchema(graphene.ObjectType):
    ChemicalID = graphene.String()
    ChemicalName = graphene.String()
    CasRN = graphene.String()

class CreateChemical(graphene.Mutation):
    class Arguments:
        ChemicalID = graphene.String(required=True)
        ChemicalName = graphene.String(required=True)
        CasRN = graphene.String(required=False)

    success = graphene.Boolean()
    chemical = graphene.Field(lambda: ChemicalSchema)

    def mutate(self, info, **kwargs):
        chemical = Chemical(**kwargs)
        chemical.save()
        return CreateChemical(chemical=chemical, success=True)

class DeleteChemical(graphene.Mutation):
    class Arguments:
        ChemicalID = graphene.String(required=True)

    success = graphene.Boolean()
    chemical = graphene.Field(lambda: ChemicalSchema)

    def mutate(self, info, ChemicalID):
        chemical = Chemical(ChemicalID=ChemicalID).fetch(ChemicalID)
        chemical.delete()
        return DeleteChemical(success=True)

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
        compound = Compound(_id=_id).fetch(int(_id))
        return CompoundSchema(**compound.as_dict())

    chemical = graphene.Field(lambda: ChemicalSchema, ChemicalID=graphene.String())
    def resolve_chemical(root, info, ChemicalID):
        chemical = Chemical(ChemicalID=ChemicalID).fetch(ChemicalID)
        return ChemicalSchema(**chemical.as_dict())

    chemicals = graphene.List(lambda: ChemicalSchema)
    def resolve_chemicals(self, info, **kwargs):
        chemicals = Chemical().all
        return [ChemicalSchema(**chemical.as_dict()) for chemical in chemicals]

class Mutations(graphene.ObjectType):
    create_compound = CreateCompound.Field()
    create_chemical = CreateChemical.Field()
    delete_chemical = DeleteChemical.Field()

schema = graphene.Schema(query=Query, mutation=Mutations).graphql_schema