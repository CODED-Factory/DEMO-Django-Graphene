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

    def resolve_thing(self, info):
        return datetime.now()

    def resolve_instructors(self, info):
        return Instructor.objects.all()
