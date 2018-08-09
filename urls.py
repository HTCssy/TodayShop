from django.conf.urls import url, include
from django.contrib import admin

from apps.df_user import views
import xadmin

urlpatterns = [
    url('admin/', xadmin.site.urls),
    url('^$', views.index, name='index'),
    url('shop/', include('apps.df_user.urls')),
]
