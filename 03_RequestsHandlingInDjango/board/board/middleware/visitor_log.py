import datetime


class VisitorLog:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path
        method = request.method
        datetime_response = datetime.datetime.now()
        response = self.get_response(request)
        with open('visitorlog.txt', 'a', encoding='utf-8') as f:
            f.write('{} {} {}'.format(datetime_response, path, method) + '\n')

        return response
