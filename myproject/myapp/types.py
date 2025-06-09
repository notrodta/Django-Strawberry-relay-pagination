import strawberry_django
from myapp import models

@strawberry_django.type(models.Book)
class BookType:
    id: int
    title: str
    author: str