import strawberry
import strawberry_django 
from strawberry_django.relay import DjangoCursorConnection
from myapp.types import BookType

@strawberry.type
class Query:
    # books: strawberry.relay.ListConnection[BookType] = strawberry_django.connection()
    books: DjangoCursorConnection[BookType] = strawberry_django.connection()


schema = strawberry.Schema(query=Query)