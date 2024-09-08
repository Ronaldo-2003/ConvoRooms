from django.http import HttpResponse

def home(request):
    return HttpResponse("<h3>Dear user , you are at home page.</h3>")