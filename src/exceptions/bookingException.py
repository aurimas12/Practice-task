from rest_framework.exceptions import APIException


class BadRequestException(APIException):
    status_code = 400
    default_detail = "Service temporarily unavailable, try again later."
