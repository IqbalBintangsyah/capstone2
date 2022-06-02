from django.urls import path
from . import views
app_name = 'feature'

urlpatterns = [
    path('lahar/', views.lahar, name="lahar"),
    path('lava/', views.lava, name="lava"),
    path('piroklastik/', views.piroklastik, name="piroklastik"),
    path('laharapi/', views.my_django_view, name="my_django_view"),
]