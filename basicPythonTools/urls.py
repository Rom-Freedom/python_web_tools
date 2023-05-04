from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, "yyyy")
register_converter(converters.MyFloatConverter, "my_float")
register_converter(converters.MyDateConverter, "my_date")

urlpatterns = [
    path('', views.index, name='python_index'),
    path("<my_date:web_tool>", views.get_my_date_converters),
    path("<yyyy:web_tool>", views.get_yyyy_converters),
    path("<int:web_tool>", views.show_information_about_tool_by_number),
    path("<my_float:web_tool>", views.get_my_float_converters),
    path("<str:web_tool>", views.show_information_about_tool, name='python_tools'),

]