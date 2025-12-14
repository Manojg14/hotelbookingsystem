from django.urls import path
from django.urls import path, include

from . import views

urlpatterns = [
    
    path('accounts/', include('allauth.urls')),  # <- required for Google login
    #path('', include('hotelapp.urls')),
    
    path('', views.home, name='home'),
    path('form/', views.booking_list, name='user_list'),
    path('view/', views.view_list, name='view_list'),
    path('contact/', views.contact_view, name='contact'),

    path('login/', views.login_register_page, name='login_register'),
    path('logout/', views.logout_view, name='logout'),  # <-- Add this


    path('login/submit/', views.login_view, name='login_submit'),
    path('register/submit/', views.register_form, name='register_submit'),

    path('view/update/<int:id>/', views.update, name='update'),
    path('view/delete/<int:id>/', views.delete, name='delete'),
    
]

