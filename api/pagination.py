from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 5  # Número de elementos por página
    page_size_query_param = 'page_size'  # Parámetro de consulta para el tamaño de página
    max_page_size = 100  # Tamaño máximo de página permitido
    page_query_param = 'page'  # Parámetro de consulta para la página actual