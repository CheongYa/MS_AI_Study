from django.urls import path, re_path
from ai.apis.v1.common import HelloWorldView

urlpatterns = [
    path(r'helloworld/', HelloWorldView.as_view(), name='helloWorld'),
]