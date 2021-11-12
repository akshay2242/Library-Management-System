from app1.api.serializers import BookSerializer
from app1.models import Books
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser

# All Books View 
class AllBooks(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]