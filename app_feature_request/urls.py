from django.conf.urls import url
import views

app_name='app_feature_request'

urlpatterns = [
    url(r'^$', views.index, name='home'),
]


