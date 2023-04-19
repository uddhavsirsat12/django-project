from django.urls import path
from .views import home, user_login, sucess, signup, user_logout
urlpatterns = [
    path('home/', home, name='home'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('sucess/', sucess, name='sucess'),
    path('signup/', signup, name='signup'),
]