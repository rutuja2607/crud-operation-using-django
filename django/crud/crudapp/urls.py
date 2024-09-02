from django.urls import path,include
from . import views
urlpatterns = [
    
    path('', views.index),
    path ('add/',views.add,name='add'),
    path('edit',views.edit,name='edit'),
    path('update/<str:id>',views.update,name='update'),
    path ('delete/<str:id>',views.delete,name='delete'),

]
