from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'blog.views.post_list'),
    url(r'^(?P<pk>\d+)/$', 'blog.views.post_detail'),
]
