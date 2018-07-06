from django.conf.urls import url
from qa_app import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^answer/$', views.answer),
]
