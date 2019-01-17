from api_commons.dto import BaseDto
from rest_framework import serializers


class HelloResponseDto(BaseDto):

    message = serializers.CharField(required=True)

    def __init__(self, message: str, **kwargs):
        super().__init__(**kwargs)
        self.message = message
