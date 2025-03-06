from rest_framework import serializers
from blogApplication.models import BlogApp


class BlogAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogApp
        # you can use fields to '__all__' if you want everything from field
        # fields = '__all__'
        fields = ['id', 'title', 'blog', 'created_date', 'updated_date']

        extra_kwargs = {
            'id': {'required': True},  # ID is mandatory to identify the instance
            'title': {'required': False, 'allow_null': True},
            'blog': {'required': False, 'allow_null': True},
        }
