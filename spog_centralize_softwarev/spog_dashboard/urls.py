from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from .views import CustomLoginView
#from .views import zoho_shift_ingest_view

urlpatterns = [
    path('superadmin/', views.superadmin_dashboard, name='superadmin_dashboard'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('client-view/', views.client_dashboard, name='client_view'),
    path('client-login/', views.client_login, name='client_login'),
    #path('accounts/login/', auth_views.LogoutView.as_view(), name='logout'),
    #path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
      #path('spog_dashboard/', views.spog_dashboard, name='spog_dashboard'),
    # path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    #path('logout/', LogoutView.as_view(), name='logout'),
    #path('security/', views.security_dashboard, name='security_dashboard'),
   # path('zoho/', views.zoho_dashboard, name='zoho_dashboard'),
    #path('zoho/', views.zoho_data_view, name='zoho_dashboard'),
   # path('zoho_data/', views.zoho_data_view, name='zoho_data'),
   # path('zoho/shifts/ingest/', zoho_shift_ingest_view, name='zoho_shift_ingest'),

]