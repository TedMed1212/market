from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

def index(request):
    logger.info("Начальная страница просмотренна")
    return render(request, 'mymarket/index.html')

def about(request):
    logger.info("Вторая страница была просмотренна")
    return render(request, 'mymarket/about.html')

def about(request):
    return render(request, 'about.html')

def account(request):
    return render(request, 'account.html')
