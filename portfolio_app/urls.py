from django.urls import path
from .views import portfolio_index

urlpatterns = [
    path('', portfolio_index, name='index_page'),
]
