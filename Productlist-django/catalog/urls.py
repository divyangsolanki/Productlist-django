from django.conf.urls import url
from catalog import views

urlpatterns = [
    url(r'^products/$', views.ProductList.as_view(),name='product'),
    url(r'^products/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view(),name='productdetail'),
    url(r'^products/(?P<pk>[0-9]+)/reviews/$',views.ReviewList.as_view()),
    url(r'^products/(?P<pk>[0-9]+)/reviews/(?P<review_id>[0-9]+)/$',views.ReviewDetail.as_view()),
]
