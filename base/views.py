from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *


def all_authors(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors,many=True)
    return Response(serializer.data)