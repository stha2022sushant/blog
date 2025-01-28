from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 5  # Default items per page
    page_size_query_param = 'page_size'  # Allow the client to set the page size
    max_page_size = 100  # Maximum page size allowed
