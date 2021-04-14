from django.urls import path
from . import views

urlpatterns = [
    path('', views.read, name='read'),
    path('form_add', views.form_add, name='form_add'),
    path('form_update', views.form_update, name='form_read'),
    path('add', views.add, name='add'),
    path('update', views.update, name='update'),
    path('delete', views.delete, name='delete')
]
