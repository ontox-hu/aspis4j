import graphene
from neo4j_store import Chemical, Gene, Disease, Pathway, Collection

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
## Disease Schema

class DiseaseSchema(graphene.ObjectType):
    DiseaseID = graphene.String()
    DiseaseName = graphene.String()
    Definition = graphene.String()
    AltDiseaseIDs = graphene.String()
    Synonyms = graphene.String()
    SlimMappings = graphene.String()

class CreateDisease(graphene.Mutation):
    class Arguments:
        DiseaseID = graphene.String(required=True)
        DiseaseName = graphene.String(required=True)
        Definition = graphene.String(required=False)
        AltDiseaseIDs = graphene.String(required=False)
        Synonyms = graphene.String(required=False)
        SlimMappings = graphene.String(required=False)

    success = graphene.Boolean()
    disease = graphene.Field(lambda: DiseaseSchema)

    def mutate(self, info, **kwargs):
        disease = Disease(**kwargs)
        disease.save()
        return CreateDisease(disease=disease, success=True)

class DeleteDisease(graphene.Mutation):
    class Arguments:
        DiseaseID = graphene.String(required=True)

    success = graphene.Boolean()
    disease = graphene.Field(lambda: DiseaseSchema)

    def mutate(self, info, DiseaseID):
        disease = Disease(DiseaseID=DiseaseID).fetch(DiseaseID)
        disease.delete()
        return DeleteDisease(success=True)


##################################################################
## Pathway Schema

class PathwaySchema(graphene.ObjectType):
    PathwayID = graphene.String()
    PathwayName = graphene.String()

class CreatePathway(graphene.Mutation):
    class Arguments:
        PathwayID = graphene.String(required=True)
        PathwayName = graphene.String(required=True)

    success = graphene.Boolean()
    pathway = graphene.Field(lambda: PathwaySchema)

    def mutate(self, info, **kwargs):
        pathway = Pathway(**kwargs)
        pathway.save()
        return CreatePathway(pathway=pathway, success=True)

class DeletePathway(graphene.Mutation):
    class Arguments:
        PathwayID = graphene.String(required=True)

    success = graphene.Boolean()
    pathway = graphene.Field(lambda: PathwaySchema)

    def mutate(self, info, PathwayID):
        pathway = Pathway(PathwayID=PathwayID).fetch(PathwayID)
        pathway.delete()
        return DeletePathway(success=True)

##################################################################
## Collection Schema

class CollectionSchema(graphene.ObjectType):
    CollectionID = graphene.String()
    CollectionName = graphene.String()

class CreateCollection(graphene.Mutation):
    class Arguments:
        CollectionID = graphene.String(required=True)
        CollectionName = graphene.String(required=True)

    success = graphene.Boolean()
    collection = graphene.Field(lambda: CollectionSchema)

    def mutate(self, info, **kwargs):
        collection = Collection(**kwargs)
        collection.save()
        return CreateCollection(collection=collection, success=True)

class DeleteCollection(graphene.Mutation):
    class Arguments:
        CollectionID = graphene.String(required=True)

    success = graphene.Boolean()
    collection = graphene.Field(lambda: CollectionSchema)

    def mutate(self, info, CollectionID):
        collection = Collection(CollectionID=CollectionID).fetch(CollectionID)
        collection.delete()
        return DeleteCollection(success=True)


##################################################################

class Query(graphene.ObjectType):

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

    ## Disease queries

    disease = graphene.Field(lambda: DiseaseSchema, DiseaseID=graphene.String())
    def resolve_disease(root, info, DiseaseID):
        disease = Disease(DiseaseID=DiseaseID).fetch(DiseaseID)
        return DiseaseSchema(**disease.as_dict())

    diseases = graphene.List(lambda: DiseaseSchema)
    def resolve_diseases(self, info, **kwargs):
        diseases = Disease().all
        return [DiseaseSchema(**disease.as_dict()) for disease in diseases]

    ## Pathway queries

    pathway = graphene.Field(lambda: PathwaySchema, PathwayID=graphene.String())
    def resolve_pathway(root, info, PathwayID):
        pathway = Pathway(PathwayID=PathwayID).fetch(PathwayID)
        return PathwaySchema(**pathway.as_dict())

    pathways = graphene.List(lambda: PathwaySchema)
    def resolve_pathways(self, info, **kwargs):
        pathways = Pathway().all
        return [PathwaySchema(**pathway.as_dict()) for pathway in pathways]

    ## Collection queries

    collection = graphene.Field(lambda: CollectionSchema, CollectionID=graphene.String())
    def resolve_collection(root, info, CollectionID):
        collection = Collection(CollectionID=CollectionID).fetch(CollectionID)
        return CollectionSchema(**collection.as_dict())

    collections = graphene.List(lambda: CollectionSchema)
    def resolve_collections(self, info, **kwargs):
        collections = Collection().all
        return [CollectionSchema(**collection.as_dict()) for collection in collections]

class Mutations(graphene.ObjectType):

    # Chemical mutations

    create_chemical = CreateChemical.Field()
    delete_chemical = DeleteChemical.Field()

    # Gene mutations

    create_gene = CreateGene.Field()
    delete_gene = DeleteGene.Field()

    # Disease mutations

    create_disease = CreateDisease.Field()
    delete_disease = DeleteDisease.Field()

    # Pathway mutations

    create_pathway = CreatePathway.Field()
    delete_pathway = DeletePathway.Field()

    # Collection mutations

    create_collection = CreateCollection.Field()
    delete_collection = DeleteCollection.Field()

schema = graphene.Schema(query=Query, mutation=Mutations).graphql_schema