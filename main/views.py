from django.http import HttpResponse
from django.shortcuts import render, redirect

from main.models import ApplicationSetting


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    try:
        app_title = ApplicationSetting.objects.get(config_key='APP_TITLE')
    except ApplicationSetting.DoesNotExist:
        app_title = None
    return render(request, 'index.html', {'app_title': app_title})

def search(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword', '').strip()
        if 'hack4fun' in keyword:
            ApplicationSetting.objects.update_or_create(
                config_key='APP_TITLE',
                defaults={'config_value': keyword}
            )
    return redirect('home')
