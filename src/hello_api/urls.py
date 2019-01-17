from django.urls import path, include

urlpatterns = [
    path('', include('hello_api.hello.urls'))
]