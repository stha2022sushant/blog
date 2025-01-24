from rest_framework import serializers
from blogApplication.models import BlogApp


class BlogAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogApp
        # you can use fields to '__all__' if you want everything from field
        # fields = '__all__'
        fields = ['id', 'title', 'blog', 'created_date', 'updated_date']
