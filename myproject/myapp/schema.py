import strawberry
import strawberry_django 
from strawberry_django.relay import DjangoListConnection
from myapp.types import BookType

@strawberry.type
class Query:
    # books: ListConnectionWithTotalCount[BookType] = strawberry_django.field()
    books: strawberry.relay.ListConnection[BookType] = strawberry_django.connection()

schema = strawberry.Schema(query=Query)