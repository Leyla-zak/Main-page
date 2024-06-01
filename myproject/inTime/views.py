from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")
def login(request):
    return render(request, "Login.html")
def signin(request):
    return render(request, "SignUp.html")
def calen(request):
    return render(request, "MyCalendar.html")
def mypages(request):
    return render(request, "MyPages.html")

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Bookmark
from .serializers import BookmarkSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def bookmark_list(request):
    if request.method == 'GET':
        bookmarks = Bookmark.objects.filter(user=request.user)
        serializer = BookmarkSerializer(bookmarks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookmarkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def bookmark_detail(request, pk):
    try:
        bookmark = Bookmark.objects.get(pk=pk, user=request.user)
    except Bookmark.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookmarkSerializer(bookmark)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        bookmark.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)