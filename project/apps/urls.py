
from django.conf.urls import url, include

urlpatterns = [
    url('',include("project.apps.order.urls")),
]
