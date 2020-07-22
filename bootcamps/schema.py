from datetime import datetime
from graphene import DateTime, List, Field, Int
from graphene_django import DjangoObjectType, DjangoListField

from .models import Instructor, Cohort


class CohortType(DjangoObjectType):
    class Meta:
        model = Cohort


class InstructorType(DjangoObjectType):
    class Meta:
        model = Instructor


class Query(object):
    thing = DateTime()
    instructors = DjangoListField(InstructorType)
    instructor = Field(InstructorType, id=Int())

    def resolve_thing(self, info):
        return datetime.now()

    def resolve_instructor(self, info, id):
        if id is not None:
            return Instructor.objects.get(pk=id)
        return None
