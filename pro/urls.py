from . import views
from django.urls import path

app_name='pro'
urlpatterns=[
    path('', views.IndexClassView.as_view(), name='index'),
    path('<int:pk>', views.FoodView.as_view(), name='detail'),
    path('add/', views.CreateItem.as_view(), name='create_item'),
    path('update/<int:pk>', views.UpdateItem.as_view(), name='update'),
    path('delete/<int:pk>', views.DeleteItem.as_view(),name='delete'),
    path('product/', views.item_list, name='product')
]