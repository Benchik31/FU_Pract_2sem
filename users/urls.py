from django.urls import path
from .views import signup, login, signout

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('signout/', signout, name='signout'),
]


