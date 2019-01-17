from django.urls import path

from hello_api.hello.controllers import HelloSlugController, EchoController
from .controllers import SimpleHelloController

urlpatterns = [
    path('', SimpleHelloController.as_view()),
    path('hello/<slug>', HelloSlugController.as_view()),
    path('post', EchoController.as_view()),
]
