from django.urls import path
from . import views

urlpatterns = [
    path('createschema/',views.CreateSchema.as_view())
]
