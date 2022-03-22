import settings
from flask import Flask
from graphql_server.flask import GraphQLView


from schema import schema

app = Flask(__name__)
app.debug = True

# TODO issue 61 block - https://github.com/lmcgartland/graphene-file-upload/pull/61
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)

if __name__ == '__main__':
    app.run(host=settings.BIND_HOST,port=settings.BIND_PORT)