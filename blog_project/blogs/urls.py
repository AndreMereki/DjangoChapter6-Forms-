from django.urls import path
from . import views 

urlpatterns = [
    path("", views.HomePage.as_view(), name="Home"),
    path("post/<int:pk>/", views.BlogDetailView.as_view(), name='post'),
]