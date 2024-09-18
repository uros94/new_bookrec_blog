from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', auth_views.LoginView.as_view(), name='login'),
    path(r'^signup/$', views.signup, name='signup'),
    path(r'^logout/$', auth_views.LogoutView.as_view(), {'next_page': '/'}, name='logout'),
    path(r'^home/$', views.home, name='home'),
    path(r'^home/(?P<idb>\d+)/$', views.book_detail, name='book_detail'),
]
