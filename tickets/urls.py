from django.conf.urls import url, include
from .views import all_tickets, one_ticket, create_ticket, create_feature, add_comment_to_ticket


urlpatterns = [
    url(r'^$', all_tickets, name='tickets'),
    url(r'^(?P<ticket_id>\d+)/$', one_ticket, name='ticket'),
    url(r'^create_ticket/$', create_ticket, name='create_ticket'),
    url(r'^create_feature/$', create_feature, name='create_feature'),
    url(r'^(?P<ticket_id>\d+)/comment/$', add_comment_to_ticket, name='add_comment_to_ticket'),
]