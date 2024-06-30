from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status, serializers

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        if isinstance(exc, serializers.ValidationError):
            response.data = {
                'errors': response.data,
                'message': 'Validation error occurred',
            }
        elif response.status_code == status.HTTP_404_NOT_FOUND:
            response.data = {
                'message': 'Contact not found',
                'details': response.data,
            }
        else:
            response.data = {
                'message': 'An error occurred',
                'details': response.data,
            }
    return response
