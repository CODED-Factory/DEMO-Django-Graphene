# Django Graphene

[Slides](https://docs.google.com/presentation/d/1VSIVg2qiLdnCGM2CWiNykEeSzUyJgF-e7iVEyTHdHCA/edit?usp=sharing)

### Setup

1. Install Django Graphene

   ```shell
   pip install graphene-django
   ```

   `settings.py`

   ```python
   INSTALLED_APPS = [
       ...
       'django.contrib.staticfiles', # Required for GraphiQL
       'graphene_django'
   ]
   ```

2. Add a GraphQL url

   ```python
   from django.views.decorators.csrf import csrf_exempt
   from graphene_django.views import GraphQLView

   urlpatterns = [
       ...
       path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
   ]
   ```

3. Add an empty `Query`

   `schema.py`

   ```python
   import graphene

   class Query(graphene.ObjectType):
       pass

   schema = graphene.Schema(query=Query)
   ```

   `settings.py`

   ```python
   GRAPHENE = {
     'SCHEMA': 'graphene_demo.schema.schema'
   }
   ```

### Basics

4. Add some fields to the query

   ```python
   class Query(graphene.ObjectType):
     hello = graphene.String()
     goodbye = graphene.String()
   ```

5. Add resolvers for the fields

   ```python
   class Query(graphene.ObjectType):
     hello = graphene.String()
     goodbye = graphene.String()

     def resolve_hello(self, info):
         return "Hello world!"

     def resolve_goodbye(self, info):
         return "Goodbye cruel world!"
   ```

6. Make a field and resolver with parameters

   ```python
   class Query(graphene.ObjectType):
     hello = graphene.String(name=graphene.String(default_value="world"))
     goodbye = graphene.String()

     def resolve_hello(self, info, name):
         return f"Hello {name}!"

     def resolve_goodbye(self, info):
         return "Goodbye cruel world!"
   ```

### Django Specific

7. Make an application schema and connect it to the main schema

   `bootcamps/schema.py`

   ```python
   from datetime import datetime
   import graphene

    class Query(object):
      thing = graphene.Date()

      def resolve_thing(parent, info):
        return datetime.now()
   ```

   `schema.py`

   ```python
   import bootcamps.schema

   class Query(bootcamps.schema.Query, graphene.ObjectType):
     ...
   ```

8. Create our first type

   `bootcamps/schema.py`

   ```python
   from graphene_django import DjangoObjectType

   from .models import Instructor
   ```


    class InstructorType(DjangoObjectType):
        class Meta:
            model = Instructor
    ```

9. Add an `instructors` query

   ```python
   class Query(object):
     ...
     instructors = graphene.List(InstructorType)

     ...

     def resolve_instructors(self, info):
         return Instructor.objects.all()
   ```

10. Add a single `instructor` query

    ```python
    class Query(object):
     ...
     instructor = graphene.Field(InstructorType, id=graphene.Int())

     ...

     def resolve_instructor(self, info, id):
        if id is not None:
            return Instructor.objects.get(pk=id)
        return None
    ```
