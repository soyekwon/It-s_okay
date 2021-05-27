from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    # path('board/', views.board, name='board'),
    path('list/', views.board_list, name='board_list'),
    path('write/', views.board_write, name='board_write'),

]