from django.shortcuts import render
from .fetch import fetch_content


def home(request):
    return render(request,
                  'zena/home.html')


def news(request):
    news_url = "http://www.aau.edu.et/"
    news_info_list = fetch_content(news_url)
    return render(
        request,
        'zena/news.html',
        {'news_info_list': news_info_list})


def announcements(request):
    announcements_url = "http://www.aau.edu.et/blog/category/announcements/"
    announcements_info_list = fetch_content(announcements_url)

    return render(
        request,
        'zena/announcements.html',
        {'announcements_info_list': announcements_info_list})
