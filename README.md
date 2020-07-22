# Django Graphene

[Slides](https://docs.google.com/presentation/d/1VSIVg2qiLdnCGM2CWiNykEeSzUyJgF-e7iVEyTHdHCA/edit?usp=sharing)

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
       path("graphql", csrf_exempt(GraphQLView.as_view())),
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
     'SCHEMA': 'django_root.schema.schema'
   }
   ```
