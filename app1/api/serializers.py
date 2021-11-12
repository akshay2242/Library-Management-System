from rest_framework import serializers
from app1.models import Books

# Book Serializer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id','title', 'author_name','published_date', 'available_status']
     
     