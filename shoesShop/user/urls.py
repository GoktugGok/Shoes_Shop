from django.urls import path

from user import views

urlpatterns = [
    path("", views.user_profile, name="user_profile"),
    path('update/', views.user_update, name='user_update'),
    # path('password/', views.user_password, name='user_password'),
    path('mycomments/', views.user_comments, name='user_comments'),
    path('deletecomment/<int:id>', views.user_deletecomment, name='user_deletecomment'),
]