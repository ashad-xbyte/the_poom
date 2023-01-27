from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('sales/', views.sales, name='sales'),
    path('production/', views.production, name='production'),
    path('devloper/', views.devloper, name='devloper'),
    path('client/', views.client, name='client'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)