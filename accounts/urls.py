from django.conf.urls import url,include
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$',views.home),
    url(r'^login/$',login,{'template_name':'accounts/login.html'}),
    url(r'^home/$',views.home),
    #url(r'^logout/$',logout,{'template_name':'accounts/logout.html'}),
    url(r'^register/$',views.register,name='register'),
    url(r'^jiraOnCall/$',views.jiraOnCall),
    url(r'^oauth/$', include('social_django.urls', namespace='social')),  # <--

]
