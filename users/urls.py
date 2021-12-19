from django.urls import path

from .views import SingupPageView

urlpatterns = [
    path('singup/', SingupPageView.as_view(), name='singup')
]