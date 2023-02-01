from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
#class Pong(View):
#    def get(self,request):
#        return HttpResponse("pong")

@require_http_methods(["GET","HEAD","OPTIONS"])
def pong(request):
    if request.method in ["GET","HEAD"]:
        return HttpResponse("pong")
    else:
        response = HttpResponse()
        response["Allow"] = ", ".join(["GET","HEAD","OPTIONS"])
        return response

class Status(TemplateView):
    extra_context = {"status":"Good"}
    template_name = "testapp/status.html"