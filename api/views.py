'''
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from blogApplication.models import BlogApp
from .serializers import BlogAppSerializer


@api_view(['GET'])
def getBlogs(request):
    blogs = BlogApp.objects.all()
    serializer = BlogAppSerializer(blogs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getBlogsPartial(request, pk):
    blogs = BlogApp.objects.get(id=pk)
    serializer = BlogAppSerializer(blogs, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addBlogs(request):
    serializer = BlogAppSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def updateBlogs(request, pk):
    blogs = BlogApp.objects.get(id=pk)
    serializer = BlogAppSerializer(instance=blogs, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteBlogs(request, pk):
    blogs = BlogApp.objects.get(id=pk)
    blogs.delete()
    return Response('Blog Successfully Deleted !')

'''

from rest_framework.viewsets import ModelViewSet
from blogApplication.models import BlogApp
from .serializers import BlogAppSerializer


class BlogAppViewSet(ModelViewSet):
    """
    A viewset for viewing, creating, updating, and deleting blog instances.
    """
    queryset = BlogApp.objects.all()
    serializer_class = BlogAppSerializer

