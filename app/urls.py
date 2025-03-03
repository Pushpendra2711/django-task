from django.urls import path
from . import views

urlpatterns = [
    path('data/',views.get_data),
    path('protected/',views.protected_view.as_view(),name='protected_view')
]