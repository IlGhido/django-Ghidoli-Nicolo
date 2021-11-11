from django.urls.conf import path

from .views import es_if
from .views import if_else_elif
from .views import es_for


app_name="seconda_app"

urlpatterns = [
    path("es_if",es_if,name="es_if"),
    path("if_else_elif",if_else_elif,name="if_else_elif"),
    path("es_for",es_for,name="es_for"),
]