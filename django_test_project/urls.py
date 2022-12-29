
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path
from blog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/customers/$', views.customers_list),
	url(r'^api/customers/(?P<pk>[0-9]+)$', views.customers_detail)
]
