import urllib.parse

from api_commons.common import ApiResponse
from django.http import HttpRequest

from hello_api.common import BaseHelloController
from hello_core.services.HelloService import HelloService
from .dto import HelloResponseDto

_helloService = HelloService()


class SimpleHelloController(BaseHelloController):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, request: HttpRequest):
        message = _helloService.sayHello()
        return ApiResponse.success(HelloResponseDto(message))


class HelloSlugController(BaseHelloController):

    def get(self, request: HttpRequest, slug: str):
        message = _helloService.sayHello(slug)
        return ApiResponse.success(HelloResponseDto(message))


class EchoController(BaseHelloController):

    URL_ENCODED_CONTENT_TYPES = ['application/x-www-form-urlencoded', 'multipart/form-data']

    def post(self, request: HttpRequest):
        try:
            decoded_body = request.body.decode("utf-8")

            if request.content_type in self.URL_ENCODED_CONTENT_TYPES:
                decoded_body = urllib.parse.unquote_plus(decoded_body)  #self._query_dict_to_str(request.POST)

            message = _helloService.echo(decoded_body)
            return ApiResponse.success(HelloResponseDto(message))

        except UnicodeDecodeError:
            return ApiResponse.bad_request('Cannot convert POST data to string')
