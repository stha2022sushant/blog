from rest_framework.viewsets import ModelViewSet
from blogApplication.models import BlogApp
from .serializers import BlogAppSerializer

from rest_framework.response import Response
from rest_framework import status


class BlogAppViewSet(ModelViewSet):
    """
    A viewset for viewing, creating, updating, and deleting blog instances.
    """
    queryset = BlogApp.objects.all()
    serializer_class = BlogAppSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"detail": "Blog deleted successfully."},
                        status=status.HTTP_200_OK)
