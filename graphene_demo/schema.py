from graphene import ObjectType, Schema

from graphql_auth.schema import MeQuery
from graphql_auth import mutations

from bootcamps.schema import Query as BootcampQuery


class Query(MeQuery, BootcampQuery, ObjectType):
    pass


class Mutation(ObjectType):
    register = mutations.Register.Field()
    login = mutations.ObtainJSONWebToken.Field()


schema = Schema(query=Query, mutation=Mutation)
