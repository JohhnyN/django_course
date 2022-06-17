import time

from django.core.exceptions import PermissionDenied


class VisitorLog:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        path = request.path
        method = request.method
        headers = request.headers
        print(headers)

        response = self.get_response(request)
        with open('visitorlog.txt', 'a', encoding='utf-8') as f:
            f.write('{} {} {}'.format(ip, path, method) + '\n')

        return response


