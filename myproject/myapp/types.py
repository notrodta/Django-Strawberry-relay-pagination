import strawberry
import strawberry_django
from strawberry.relay import Node
from myapp import models

@strawberry_django.type(models.Book, pagination=True)
class BookType(Node):
    title: strawberry.auto
    author: strawberry.auto