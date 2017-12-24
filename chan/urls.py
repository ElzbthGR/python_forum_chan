from django.conf.urls import url
from . import views


app_name = 'chan'
urlpatterns = [
    url(r'^$', views.show_messages, name = 'show_messages'),
    url(r'^reply/(?P<message_id>\d+)/', views.reply, name = 'reply'),
    url(r'^new_record/', views.new_record, name = 'new_record')
]