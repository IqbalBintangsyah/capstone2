
from django.urls import path
from . import views
app_name = 'about'

urlpatterns = [
    path('website/', views.about, name="website"),
    path('team/', views.team, name="team"),
    path('informasigunung/', views.informasigunung, name="informasigunung"),
]