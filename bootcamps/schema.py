from graphene import List, Field, Int, String
from graphene_django import DjangoObjectType, DjangoListField

from .models import Instructor, Cohort, Bootcamp, Role, Topic


class BootcampType(DjangoObjectType):
    class Meta:
        model = Bootcamp


class CohortType(DjangoObjectType):
    class Meta:
        model = Cohort


class InstructorType(DjangoObjectType):
    slug = String()
    bio = String

    class Meta:
        model = Instructor

    def resolve_slug(self, info):
        return self.name.lower()

    def resolve_bio(self, info):
        if info.context.user.is_authenticated:
            return self.bio
        return "شتبي"


class RoleType(DjangoObjectType):
    class Meta:
        model = Role


class TopicType(DjangoObjectType):
    class Meta:
        model = Topic


class Query(object):
    bootcamps = DjangoListField(BootcampType)
    cohorts = DjangoListField(CohortType)
    instructors = DjangoListField(InstructorType)
    topics = DjangoListField(TopicType)
    instructor = Field(InstructorType, id=Int(), name=String())

    def resolve_date(self, info):
        return datetime.now().date()

    def resolve_instructor(self, info, id=None, name=None):
        if id is not None:
            return Instructor.objects.get(pk=id)
        if name is not None:
            return Instructor.objects.get(name=name)
        return None
