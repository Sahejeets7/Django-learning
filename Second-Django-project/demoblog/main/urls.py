from django.urls import path
from . import views
from django.views.generic import ListView,DetailView
from .models import Topic

app_name = 'main'

urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('register/',views.register,name='register'),
    path('login/',views.login_request,name='login'),
    path('logout/',views.logout_request,name='logout'),
    path('<int:pk>/',DetailView.as_view(model=Topic,template_name="main/info.html")),
    # path('/')
]
