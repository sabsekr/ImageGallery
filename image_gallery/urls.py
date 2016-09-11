from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

"""
ex: /imagegallery/5/

ex: /imagegallery/add/
"""


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^(?P<pk>[0-9]+)/$', views.ShowPhotoView.as_view(), name='showphoto'),

    url(r'^add/$', views.upload_pic, name='upload_pic'),

]
