from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page, name='home_page'),
    path('news/all/',views.news_page, name='news_page'),
    path('news/detail/<int:pk>',views.details_page, name='details_page'),
    path('user/sign_up/', views.sign_up_page, name='sign_up_page'),
    path('user/login/', views.login_page, name='login_page'),
    path('user/logout/', views.logout_request, name='logout_request'),

]