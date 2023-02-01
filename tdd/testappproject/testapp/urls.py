from django.urls import path
#from .views import Pong
from .views import pong
from .views import Status
urlpatterns = [
    path("ping/",pong, name="ping"),
    path("status/",Status.as_view(),name="site_status")
    #path("ping/",Pong.as_view(), name="ping")
]