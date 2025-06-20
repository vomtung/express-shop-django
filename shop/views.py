from django.http import HttpResponse
from django.shortcuts import render

from main.models import ApplicationSetting


# Create your views here.
def shop(request):
    try:
        app_title = ApplicationSetting.objects.get(config_key='APP_TITLE')
    except ApplicationSetting.DoesNotExist:
        app_title = None
    return render(request, 'index.html', {'app_title': app_title})