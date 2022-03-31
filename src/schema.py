import graphene
from neo4j_store import Chemical, Gene
from neo4j_store import Compound

##################################################################
## Chemical Schema

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

##################################################################
## Gene Schema

class GeneSchema(graphene.ObjectType):
    GeneID = graphene.String()
    GeneSymbol = graphene.String()
    GeneName = graphene.String()
    Synonyms = graphene.String()
    BioGRIDIDs = graphene.String()
    PharmGKBIDs = graphene.String()
    UniprotIDs = graphene.String()

class CreateGene(graphene.Mutation):
    class Arguments:
        GeneID = graphene.String(required=True)
        GeneSymbol = graphene.String(required=True)
        GeneName = graphene.String(required=False)
        Synonyms = graphene.String(required=False)
        BioGRIDIDs = graphene.String(required=False)
        PharmGKBIDs = graphene.String(required=False)
        UniprotIDs = graphene.String(required=False)

    success = graphene.Boolean()
    gene = graphene.Field(lambda: GeneSchema)

    def mutate(self, info, **kwargs):
        gene = Gene(**kwargs)
        gene.save()
        return CreateGene(gene=gene, success=True)

class DeleteGene(graphene.Mutation):
    class Arguments:
        GeneID = graphene.String(required=True)

    success = graphene.Boolean()
    gene = graphene.Field(lambda: GeneSchema)

    def mutate(self, info, GeneID):
        gene = Gene(GeneID=GeneID).fetch(GeneID)
        gene.delete()
        return DeleteGene(success=True)

##################################################################
## To delete later
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



##################################################################

class Query(graphene.ObjectType):

    compound = graphene.Field(lambda: CompoundSchema, _id=graphene.String())
    def resolve_compound(root, info, _id):
        compound = Compound(_id=_id).fetch(int(_id))
        return CompoundSchema(**compound.as_dict())

    ## Chemical queries

    chemical = graphene.Field(lambda: ChemicalSchema, ChemicalID=graphene.String())
    def resolve_chemical(root, info, ChemicalID):
        chemical = Chemical(ChemicalID=ChemicalID).fetch(ChemicalID)
        return ChemicalSchema(**chemical.as_dict())

    chemicals = graphene.List(lambda: ChemicalSchema)
    def resolve_chemicals(self, info, **kwargs):
        chemicals = Chemical().all
        return [ChemicalSchema(**chemical.as_dict()) for chemical in chemicals]

    ## Gene queries

    gene = graphene.Field(lambda: GeneSchema, GeneID=graphene.String())
    def resolve_gene(root, info, GeneID):
        gene = Gene(GeneID=GeneID).fetch(GeneID)
        return GeneSchema(**gene.as_dict())

    genes = graphene.List(lambda: GeneSchema)
    def resolve_genes(self, info, **kwargs):
        genes = Gene().all
        return [GeneSchema(**gene.as_dict()) for gene in genes]

class Mutations(graphene.ObjectType):
    create_compound = CreateCompound.Field()

    # Chemical mutations

    create_chemical = CreateChemical.Field()
    delete_chemical = DeleteChemical.Field()

    # Gene mutations

    create_gene = CreateGene.Field()
    delete_gene = DeleteGene.Field()


schema = graphene.Schema(query=Query, mutation=Mutations).graphql_schema