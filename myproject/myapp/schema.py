import strawberry
import strawberry_django
from myapp.types import BookType
from myapp.models import Book
from typing import List

@strawberry.type
class Query:
    books: List[BookType] = strawberry_django.field()

schema = strawberry.Schema(query=Query)