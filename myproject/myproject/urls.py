from django.contrib import admin
from django.urls import path, include
from strawberry.django.views import GraphQLView
from myapp.schema import schema
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path("graphql/", csrf_exempt(GraphQLView.as_view(schema=schema))),
]