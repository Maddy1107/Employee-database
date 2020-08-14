from django.conf.urls import url,include,handler404
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^login/', auth_views.login,name='login'),
    url(r'^logout/', auth_views.logout,{'template_name': 'personal/home1.html'}, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('personal.urls')),

]

handler404 = 'personal.views.custom_404'
