import strawberry
import strawberry_django
from strawberry_django import auth, mutations
from asgiref.sync import sync_to_async
from . models import BlogApp as BlogAppModel
from api.serializers import BlogAppSerializer

from .types import (
    BlogApp,
    BlogAppInput,
    BlogAppPartialInput,
    User,
    UserInput,
)


@strawberry.type
class Query:
    blog: BlogApp = strawberry_django.field()
    blogs: list[BlogApp] = strawberry_django.field()


@strawberry.type
class Mutation:
    create_blog: BlogApp = mutations.create(BlogAppInput)
    # create_blogs: list[BlogApp] = mutations.create(BlogAppInput)

    # update_blogs: list[BlogApp] = mutations.update(BlogAppPartialInput)

    @strawberry.mutation
    @sync_to_async
    def update_blog(self, blog_data: BlogAppPartialInput) -> BlogApp:
        # Convert the input data to a dictionary and remove keys with None values
        blog_data_dict = {key: value for key, value in blog_data.__dict__.items() if value is not None}

        try:
            # Fetch the existing instance
            blog_instance = BlogAppModel.objects.get(id=blog_data.id)
        except BlogAppModel.DoesNotExist:
            raise ValueError(f"Blog with ID {blog_data.id} does not exist.")

        # Use the serializer for validation and update
        serializer = BlogAppSerializer(instance=blog_instance, data=blog_data_dict, partial=True)
        if serializer.is_valid():
            updated_instance = serializer.save()
            return updated_instance
        else:
            # Handle validation errors
            raise ValueError(f"Invalid data: {serializer.errors}")

    @strawberry.mutation
    @sync_to_async
    def delete_blog(self, blog_id: int) -> str:
        try:
            blog_instance = BlogAppModel.objects.get(id=blog_id)
        except BlogAppModel.DoesNotExist:
            raise ValueError(f"Blog with ID {blog_id} does not exist.")

        # Optionally, use the deletion serializer to serialize the deleted blog
        serializer = BlogAppSerializer(blog_instance)
        blog_instance.delete()
        return f"Blog with ID {blog_id} and title '{serializer.data['title']}' has been deleted successfully."
    register: User = auth.register(UserInput)


schema = strawberry.Schema(query=Query, mutation=Mutation)
