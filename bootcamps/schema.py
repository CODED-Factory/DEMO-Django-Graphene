from datetime import datetime
import graphene
from graphene_django import DjangoObjectType

from .models import Instructor


class InstructorType(DjangoObjectType):
    class Meta:
        model = Instructor


class Query(object):
    thing = graphene.DateTime()
    instructors = graphene.List(InstructorType)
    instructor = graphene.Field(InstructorType, id=graphene.Int())

    def resolve_thing(self, info):
        return datetime.now()

    def resolve_instructors(self, info):
        return Instructor.objects.all()

    def resolve_instructor(self, info, id):
        if id is not None:
            return Instructor.objects.get(pk=id)
        return None
