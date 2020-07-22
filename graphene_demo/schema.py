import graphene

import bootcamps.schema


class Query(bootcamps.schema.Query, graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="world"))
    goodbye = graphene.String()

    def resolve_hello(self, info, name):
        return f"Hello {name}!"

    def resolve_goodbye(self, info):
        return "Goodbye cruel world!"


schema = graphene.Schema(query=Query)
