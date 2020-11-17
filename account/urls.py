from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

app_name = 'account'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('api/', include(router.urls)),
]
