from django.urls import path, register_converter
from app.views import file_list, file_content
from app.format_converters import FormatConverter_dt

# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам

register_converter(FormatConverter_dt, 'dt')

urlpatterns = [
    path('', file_list, name='file_list'),
    path('<dt:date>/', file_list, name='file_list'),
    path('file/<name>', file_content, name='file_content'),
    # Определите схему урлов с привязкой к отображениям .views.file_list и .views.file_content
    # path(..., name='file_list'),
    # path(..., name='file_list'),    # задайте необязательный параметр "date"
    # для детальной информации смотрите HTML-шаблоны в директории templates
    # path(..., name='file_content'),
]
