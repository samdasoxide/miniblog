from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'blogs/$', views.BlogListView.as_view(), name='all-blogs'),
    url(r'blogger/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    url(r'(?P<pk>\d+)$', views.BlogDetailView.as_view(), name='blog-detail'),
    url(r'bloggers/$', views.AuthorListView.as_view(), name='all-authors')
]
