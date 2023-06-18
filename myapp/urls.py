from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('seznam/', views.seznam, name='seznam'),
    path('seznam/<int:pk>', views.Detail_kniha.as_view(), name='kniha'),
]
