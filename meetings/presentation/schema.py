from graphene import Schema
from .queries import Queries

schema = Schema(query=Queries)
