from django.http import HttpResponseForbidden

class DebugMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        if request.method == "POST":
            print(f"DEBUG: Origin={request.headers.get('Origin')}, Host={request.get_host()}")
        return self.get_response(request)
