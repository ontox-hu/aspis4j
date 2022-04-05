## GraphDB
Currently the schema is defined at [src/neo4j_store.py](https://github.com/ontox-hu/aspis4j/blob/main/src/neo4j_store.py). 

#### Add A Node Label
Extend BaseModel in the same way that the Chemical class [neo4j_store.py line](https://github.com/ontox-hu/aspis4j/blob/main/src/neo4j_store.py#L40) extends BaseModel:
```Python
class Chemical(BaseModel):
    ...
    __primarykey__  = 'ChemicalID'
    ChemicalID = Property() 
```

#### Add A Relationship  
Add a `RelatedTo` property to a BaseModel class:

```Python
class Compound(BaseModel):
    ...
    metabolizes  = RelatedTo('Protein',"metabolizes") 
    translocates = RelatedTo('Protein',"translocates")
    is_converted = RelatedTo('Compound','is_converted_to')
    translocated_from = RelatedTo('Compound','translocated_from')
```
Properties of the compound class ([neo4j_store.py#L104](https://github.com/ontox-hu/aspis4j/blob/main/src/neo4j_store.py#L104))

## GraphQL
Aspis4J might become a federated graphql server. This project uses the python graphene package to define graphql. To modify the graphql server you could update https://github.com/ontox-hu/aspis4j/blob/main/src/schema.py. 
