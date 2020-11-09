from django.urls import path

from . import views

app_name = 'account'
urlpatterns = [
    path('', views.index, name='index'),
    path('specifics/<int:question_id>', views.detail, name='detail')
]
