from django.conf.urls import url
from . import views

app_name = 'notes'

# looking for index function
urlpatterns = [
    url('^$', views.index,kwargs='', name='index'),
    url('^details/(?P<id>\w{0,50})/$', views.details),
    url('^add', views.add, name='add'),
    url('^delete/', views.delete, name='delete'),

    #url('^delete/(?P<id>\w{0,50})/$',views.delete, name='delete')
]
