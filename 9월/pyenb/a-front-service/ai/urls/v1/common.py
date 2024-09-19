from django.urls import path, re_path
from ai.apis.v1.common import HelloWorldView, HelloWorld2View

urlpatterns = [
    path(r'helloworld/', HelloWorldView.as_view(), name='helloWorld'),
    path(r'helloworld2/', HelloWorld2View.as_view(), name='helloWorld2')
]