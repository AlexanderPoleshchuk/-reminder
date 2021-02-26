
from django.urls import path, include

from todo.views import index

urlpatterns = [
    path('', index)
]
