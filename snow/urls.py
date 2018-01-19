from django.conf.urls import url
from snow import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
